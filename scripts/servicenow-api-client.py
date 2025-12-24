#!/usr/bin/env python3
"""
ServiceNow API Client (Python)

Reusable wrapper around ServiceNow REST APIs for metric collection,
capacity analysis, and platform observability.

All values are placeholders and must be configured per environment.
"""

import os
import sys
import json
import time
import logging
from typing import Dict, Any, Optional

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger("servicenow_api_client")


class ServiceNowClient:
    def __init__(self, instance_url: str, username: str, password: str, timeout: int = 30):
        self.instance_url = instance_url.rstrip("/")
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({"Content-Type": "application/json"})
        self.timeout = timeout

    def _build_url(self, path: str) -> str:
        return f"{self.instance_url}/{path.lstrip('/')}"

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        url = self._build_url(path)
        logger.debug("GET %s params=%s", url, params)
        resp = self.session.get(url, params=params, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def paged_get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        limit: int = 1000,
    ):
        """
        Simple pagination pattern for ServiceNow table APIs.
        """
        if params is None:
            params = {}
        offset = 0
        while True:
            page_params = dict(params)
            page_params.update({"sysparm_limit": limit, "sysparm_offset": offset})
            data = self.get(path, page_params)
            records = data.get("result", [])
            if not records:
                break
            for record in records:
                yield record
            offset += len(records)


def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_client_from_env_or_config(config_path: str = "config/baseline-config.json") -> ServiceNowClient:
    """
    Priority:
    1. Environment variables
    2. baseline-config.json
    """
    instance_url = os.getenv("SN_INSTANCE_URL")
    username = os.getenv("SN_USERNAME")
    password = os.getenv("SN_PASSWORD")

    if not instance_url or not username or not password:
        logger.info("Environment variables not fully set, falling back to config file: %s", config_path)
        cfg = load_config(config_path)
        instance_url = instance_url or cfg.get("instance_url")
        username = username or cfg.get("username")
        password = password or cfg.get("password")

    if not all([instance_url, username, password]):
        logger.error("Missing ServiceNow configuration. Check environment variables or config file.")
        sys.exit(1)

    return ServiceNowClient(instance_url=instance_url, username=username, password=password)


def main():
    """
    Minimal example use of the client. In practice, this module is imported
    by other scripts (collect-metrics, data-normalization, forecasting, etc.).
    """
    client = build_client_from_env_or_config()

    # Example: fetch node metrics from a hypothetical table/view
    path = "/api/now/table/x_capacity_node_metrics"
    params = {"sysparm_query": "active=true"}

    logger.info("Fetching sample metrics from %s", path)
    try:
        for record in client.paged_get(path, params=params, limit=200):
            logger.debug("Record: %s", record)
            # In real usage, pass these records into data-normalization or storage.
            break  # only show one in example
    except requests.HTTPError as e:
        logger.error("HTTP error while calling ServiceNow: %s", e)
        sys.exit(1)

    logger.info("ServiceNow API client test completed successfully.")


if __name__ == "__main__":
    main()
