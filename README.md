<# 📊 ServiceNow Capacity Optimization Toolkit  
**Automated analytics, forecasting, and operational insights for mission‑critical ServiceNow environments**

A sanitized engineering toolkit demonstrating API automation, capacity forecasting, and cross‑platform operational workflows.

---

## ✨ Overview  
This project delivers an automated pipeline for collecting, normalizing, and forecasting ServiceNow platform capacity metrics. It provides engineers and platform owners with actionable insights into node performance, workflow execution, and saturation risks across enterprise environments.

---

## ⚡ Quick Start  
```bash
# 1. Collect metrics
python scripts/collect-metrics.py

# 2. Normalize data
python scripts/data-normalization.py

# 3. Generate forecasts
python scripts/forecasting-engine.py

# 4. Run full pipeline (Windows)
.\scripts\job-runner.ps1
```

---

## 🧾 System Summary  
The toolkit integrates with ServiceNow APIs to extract performance data, applies normalization rules for consistency, and generates capacity forecasts using lightweight analytics. It supports multi‑environment profiles, cross‑platform automation (Python + PowerShell), and modular configuration for enterprise deployments.

---

## 💡 Why This Work Matters  
ServiceNow performance directly impacts workflow execution, incident resolution, and enterprise productivity.  
This toolkit enables:

- Early detection of saturation risks  
- Data‑driven scaling decisions  
- Predictable platform performance  
- Improved user experience  
- Repeatable, auditable capacity workflows  

---

## 🎯 Responsibilities & Scope  
This repository demonstrates engineering capabilities across:

- API integration and automation  
- Data collection and normalization  
- Capacity forecasting and analytics  
- Cross‑platform scripting (Python + PowerShell)  
- Operational runbooks and troubleshooting  
- Architecture documentation and environment modeling  

---

## 🛠️ Technologies & Tools  
- **Python** — analytics, forecasting, data processing  
- **PowerShell** — automation, orchestration, Windows integration  
- **ServiceNow REST APIs** — metric extraction  
- **YAML / JSON** — configuration and environment profiles  
- **ASCII architecture diagrams** — sanitized system visualization  

### Platform Stack  
- ServiceNow (sanitized instance)  
- Local/remote compute for analytics  
- Storage for raw, normalized, and forecast datasets  

---

## 🗂️ Repository Structure  
```
ServiceNow/
│
├── architecture/
│   ├── architecture-summary.md
│   ├── architecture-layers.md
│   └── architecture-diagram.md
│
├── docs/
│   ├── deployment-overview.md
│   ├── troubleshooting-guide.md
│   ├── runbook.md
│   └── data-dictionary.md
│
├── scripts/
│   ├── servicenow-api-client.py
│   ├── servicenow-api-client.ps1
│   ├── collect-metrics.py
│   ├── collect-metrics.ps1
│   ├── data-normalization.py
│   ├── forecasting-engine.py
│   ├── analyze-capacity.ps1
│   └── job-runner.ps1
│
├── config/
│   ├── baseline-config.json
│   └── environment-profile.yaml
│
└── README.md
```

---

## ▣ Key Files  

### 📐 Architecture  
- [`architecture-summary.md`](architecture/architecture-summary.md) — High‑level system overview  
- [`architecture-layers.md`](architecture/architecture-layers.md) — Functional decomposition  
- [`architecture-diagram.md`](architecture/architecture-diagram.md) — Sanitized ASCII diagram  

### 🧰 Scripts  
- [`servicenow-api-client.py`](scripts/servicenow-api-client.py) — Python ServiceNow API wrapper  
- [`servicenow-api-client.ps1`](scripts/servicenow-api-client.ps1) — PowerShell ServiceNow API wrapper  
- [`collect-metrics.py`](scripts/collect-metrics.py) — Python metric collector  
- [`collect-metrics.ps1`](scripts/collect-metrics.ps1) — PowerShell metric collector  
- [`data-normalization.py`](scripts/data-normalization.py) — Schema normalization  
- [`forecasting-engine.py`](scripts/forecasting-engine.py) — Capacity forecasting  
- [`analyze-capacity.ps1`](scripts/analyze-capacity.ps1) — POD/server capacity analysis  
- [`job-runner.ps1`](scripts/job-runner.ps1) — End‑to‑end pipeline orchestrator  

### ⚙ Configuration  
- [`baseline-config.json`](config/baseline-config.json) — Core settings and API endpoints  
- [`environment-profile.yaml`](config/environment-profile.yaml) — Environment‑specific overrides    

---

## 🚀 Deployment Workflow

**Pipeline:** *Initialization → Configuration → Validation → Handoff*

| Stage | Description |
|-------|-------------|
| 1. Environment Preparation | Validate ServiceNow instance health, user roles, and integration credentials before deployment |
| 2. Data Source Configuration | Set up metric sources, MID Server connections, and ingestion schedules for capacity data |
| 3. Dashboard & Report Deployment | Import dashboards, configure widgets, and validate data bindings for accuracy |
| 4. Workflow & Automation Setup | Enable Flow Designer logic, scheduled jobs, and automation rules supporting capacity insights |
| 5. Metric Validation | Run data quality checks, confirm metric freshness, and validate trend accuracy across environments |
| 6. Integration Testing | Validate API calls, MID Server communication, and external system data ingestion |
| 7. Performance Review | Confirm dashboard load times, SLA adherence, and reporting responsiveness |
| 8. Documentation & Handoff | Update operational runbooks, dashboard references, and troubleshooting procedures |

---

## ✅ Key Outcomes  
- Predictable ServiceNow performance  
- Early detection of capacity risks  
- Automated, repeatable workflows  
- Clear visibility into platform health  
- Enterprise‑grade documentation and tooling  

---

## 🔓 Engineering Challenges Addressed  
- Inconsistent metric schemas  
- Limited visibility into node performance  
- Manual capacity planning  
- Fragmented automation across teams  
- Lack of forecasting capabilities  

---

## 🔐 Security & Access Controls  
- RBAC‑controlled API access  
- Encrypted metric storage (sanitized)  
- Environment‑specific profiles  
- No proprietary instance details included  

---

## 🔒 Confidentiality Notice  
All content is fully sanitized.  
No internal instance names, credentials, workflow IDs, or proprietary ServiceNow configurations are included.

---

## 👔 Professional Context  

**Suren Jewels**  
Cloud & Infrastructure Engineer • Security & Automation Specialist  

This repository showcases sanitized engineering patterns and automation workflows used in enterprise ServiceNow environments.

- **LinkedIn:** [https://www.linkedin.com/in/suren-jewels/](https://www.linkedin.com/in/suren-jewels/)
- **GitHub:** [https://github.com/Suren-Jewels](https://github.com/Suren-Jewels)
- **Email:** [SurenJewelsPro@gmail.com](mailto:SurenJewelsPro@gmail.com)

---
