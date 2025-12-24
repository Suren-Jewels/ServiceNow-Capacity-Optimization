# Troubleshooting Guide

This guide provides common issues, root causes, and resolution steps for the ServiceNow Capacity Optimization tooling. All content is fully sanitized and reflects generalized engineering patterns.

---

## ⚠️ Common Issues & Resolutions

### **1. Missing or Incomplete Metrics**
**Symptoms:**  
- Dashboards show gaps  
- Forecasting engine receives partial data  

**Possible Causes:**  
- API throttling  
- RBAC restrictions  
- MID server offline  

**Resolution:**  
- Verify API rate limits  
- Confirm user roles and permissions  
- Restart or validate MID server connectivity  

---

### **2. Forecasting Model Inaccuracy**
**Symptoms:**  
- Unexpected spikes or flatlines  
- Incorrect saturation predictions  

**Possible Causes:**  
- Insufficient historical data  
- Misconfigured thresholds  
- Outlier workloads  

**Resolution:**  
- Load additional historical metrics  
- Recalibrate model parameters  
- Apply smoothing or anomaly detection  

---

### **3. Dashboard Not Updating**
**Symptoms:**  
- Stale charts  
- Missing real-time data  

**Possible Causes:**  
- Collector jobs not running  
- Visualization layer misconfiguration  
- Storage write failures  

**Resolution:**  
- Validate scheduled jobs  
- Confirm dashboard data sources  
- Check storage permissions and capacity  

---

### **4. API Authentication Failures**
**Symptoms:**  
- 401/403 errors  
- Collector scripts failing  

**Possible Causes:**  
- Expired credentials  
- RBAC policy changes  
- Incorrect endpoint configuration  

**Resolution:**  
- Refresh API tokens  
- Validate assigned roles  
- Confirm endpoint URLs  

---

## 🧪 Validation Checklist
- API connectivity confirmed  
- Metric ingestion verified  
- Forecasting engine operational  
- Dashboards rendering correctly  
- Alerts firing at correct thresholds  

---

## 🔒 Confidentiality Notice
All troubleshooting steps are generalized. No internal identifiers, instance names, or proprietary configurations are included.
