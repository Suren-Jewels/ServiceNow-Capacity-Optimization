#!/usr/bin/env python3
"""
Collect ServiceNow performance and capacity metrics.

Uses the shared ServiceNow API client to pull logs, node stats,
workflow metrics, and query performance, then writes them to
a local or remote storage target (file, database, etc.).
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from servicenow_api_client import build_client_from_env_or_config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] collect-metrics - %(message)s",
)
logger = logging.getLogger("collect-metrics")


OUTPUT_DIR = Path("data/raw")


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def collect_node_metrics(client) -> Dict[str, Any]:
    """
    Example: query a custom table or view where node metrics are exposed.
    This is intentionally generic and sanitized.
    """
    path = "/api/now/table/x_capacity_node_metrics"
    params = {"sysparm_query": "active=true", "sysparm_fields": "node,metric_name,metric_value,timestamp"}
    logger.info("Collecting node metrics from %s", path)

    records = list(client.paged_get(path, params=params, limit=500))
    logger.info("Collected %d node metric records", len(records))
    return {"type": "node_metrics", "records": records}


def write_payload(payload: Dict[str, Any]) -> None:
    ensure_output_dir()
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    out_path = OUTPUT_DIR / f"{payload['type']}_{ts}.json"
    logger.info("Writing metrics payload to %s", out_path)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def main():
    client = build_client_from_env_or_config()

    payload = collect_node_metrics(client)
    write_payload(payload)

    logger.info("Metric collection completed successfully.")


if __name__ == "__main__":
    main()
