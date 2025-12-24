# Runbook — ServiceNow Capacity Optimization

This runbook provides operational procedures for running, validating, and maintaining the ServiceNow Capacity Optimization tooling. All content is fully sanitized and reflects generalized engineering patterns.

---

## 🟦 Purpose
To ensure consistent, predictable execution of the capacity pipeline across environments (dev/test/prod).

---

## 🟩 Pre‑Run Checks
Before running the pipeline:

- Confirm API credentials are valid  
- Verify MID server connectivity  
- Ensure storage directories exist  
- Validate environment profile (dev/test/prod)  
- Confirm Python and PowerShell dependencies  

---

## 🟨 Execution Steps

### **1. Run Metric Collection**
```bash
python scripts/collect-metrics.py
