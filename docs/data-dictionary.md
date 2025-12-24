
# 📘 **docs/data-dictionary.md**

```markdown
# Data Dictionary — ServiceNow Capacity Metrics

This document defines the schema, fields, and meaning of the metrics used in the capacity optimization pipeline. All content is fully sanitized.

---

## 🧱 Node Metrics Schema

| Field          | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| node           | string  | Logical node identifier                          |
| metric_name    | string  | Name of the metric (CPU, RAM, workflow_time)     |
| metric_value   | float   | Numeric value of the metric                      |
| timestamp      | string  | UTC timestamp of metric collection               |

---

## 🧱 Workflow Metrics Schema

| Field          | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| workflow_id    | string  | Sanitized workflow identifier                    |
| duration_ms    | int     | Execution duration in milliseconds               |
| status         | string  | Success/Failure                                  |
| timestamp      | string  | UTC timestamp                                    |

---

## 🧱 Query Performance Schema

| Field          | Type    | Description                                      |
|----------------|---------|--------------------------------------------------|
| query_name     | string  | Sanitized query identifier                       |
| execution_ms   | int     | Execution time                                   |
| rows_returned  | int     | Number of rows returned                          |
| timestamp      | string  | UTC timestamp                                    |

---

## 🧩 Notes
- All fields are sanitized and represent conceptual structures only  
- Actual ServiceNow table names and internal identifiers are intentionally omitted  
- This dictionary aligns with the normalization and forecasting pipeline  

---

## 🔒 Confidentiality Notice
All schema definitions are generalized. No proprietary ServiceNow table structures or internal naming conventions are included.
