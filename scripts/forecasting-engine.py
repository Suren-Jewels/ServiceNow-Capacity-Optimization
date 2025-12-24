#!/usr/bin/env python3
"""
Forecasting engine for ServiceNow capacity metrics.

This module consumes normalized data and generates
high-level capacity forecasts (e.g., utilization trends,
saturation risk windows, threshold crossings).

For portfolio purposes, this uses a simple rolling-average
approach; in practice, you might plug in ARIMA, Prophet,
or other time series tools.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] forecasting-engine - %(message)s",
)
logger = logging.getLogger("forecasting-engine")

NORMALIZED_DIR = Path("data/normalized")
FORECAST_DIR = Path("data/forecast")


def ensure_dirs() -> None:
    FORECAST_DIR.mkdir(parents=True, exist_ok=True)


def list_normalized_files() -> List[Path]:
    return sorted(NORMALIZED_DIR.glob("*_normalized.json"))


def simple_average_forecast(values: List[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def generate_forecast(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Highly simplified forecasting: compute an average utilization value.
    In a real environment, replace with time-series modeling.
    """
    metrics_by_name: Dict[str, List[float]] = {}

    for rec in records:
        name = rec.get("metric_name", "unknown")
        value = float(rec.get("metric_value", 0))
        metrics_by_name.setdefault(name, []).append(value)

    forecast_result = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "forecasts": []
    }

    for name, values in metrics_by_name.items():
        avg_value = simple_average_forecast(values)
        forecast_result["forecasts"].append(
            {
                "metric_name": name,
                "average_value": avg_value,
                "risk_level": "high" if avg_value > 80 else "medium" if avg_value > 60 else "low",
            }
        )

    return forecast_result


def process_file(path: Path) -> None:
    logger.info("Generating forecast from %s", path)
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    records = data.get("records", [])
    forecast = generate_forecast(records)

    out_name = path.name.replace("_normalized.json", "_forecast.json")
    out_path = FORECAST_DIR / out_name
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(forecast, f, indent=2)
    logger.info("Wrote forecast file to %s", out_path)


def main():
    ensure_dirs()
    files = list_normalized_files()
    if not files:
        logger.warning("No normalized files found in %s", NORMALIZED_DIR)
        return

    for path in files:
        process_file(path)

    logger.info("Forecasting completed.")


if __name__ == "__main__":
    main()
