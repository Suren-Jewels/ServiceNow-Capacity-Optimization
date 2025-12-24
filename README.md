# 📊 ServiceNow Capacity Optimization Toolkit  
**Automated analytics, forecasting, and operational insights for mission‑critical ServiceNow environments**

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























**Fleet-Scale Performance & Resource Management for Enterprise Infrastructure**

---

## 📌 Overview

This repository documents engineering work focused on capacity optimization, performance tuning, and infrastructure scaling for large-scale ServiceNow environments.

The work supported global enterprise operations across **1,000+ Linux and Windows servers**, ensuring stable, predictable performance under heavy workloads.

This project demonstrates senior-level cloud infrastructure engineering, automation, and data-driven optimization.

## 🎯 Responsibilities & Scope

- Analyzed compute, memory, and storage utilization across **1,000+ servers**
- Identified bottlenecks and performance degradation patterns
- Built automation to collect, normalize, and visualize capacity data
- Recommended scaling strategies for production, staging, and dev environments
- Developed migration planning logic for server consolidation
- Collaborated with SRE, Cloud, and ServiceNow platform teams
- Ensured compliance with enterprise performance and reliability standards

## 🛠️ Tools & Technologies

### Technology Stack

| Category | Technologies | Purpose |
|----------|-------------|---------|
| **🖥️ Operating Systems** | Linux (RHEL, Ubuntu)<br>Windows Server | 1,000+ server hybrid infrastructure |
| **🏢 Platform** | ServiceNow | Enterprise service management and ITSM |
| **⚙️ Automation** | 🐍 Python<br>💠 PowerShell<br>🐚 Shell scripting | Data collection, analysis, and automation |
| **📊 Monitoring** | Telemetry systems<br>Monitoring tools | Real-time performance metrics |
| **📋 Management** | CMDB<br>Asset management tools | Configuration tracking and inventory |

────────────────────────────────────────────────────────────────────────

## 🧠 System Summary

This system provides end-to-end capacity optimization for large-scale ServiceNow environments by collecting, aggregating, and analyzing performance metrics across more than **1000 Linux and Windows servers**.

Through automated data collection, forecasting models, and scaling recommendations, it ensures:
- Predictable performance
- Reduced bottlenecks
- Enterprise reliability standards across production, staging, and development environments

•••••••••••••••

## ⭐ Why This Work Matters

Large ServiceNow environments require continuous capacity oversight to prevent performance degradation, outages, and resource waste.

This work ensures that compute, memory, storage, and network resources remain healthy under heavy enterprise workloads.

**Key Benefits**:
- Early bottleneck identification
- Future demand forecasting
- Scaling action recommendations
- Strengthened platform reliability
- Reduced operational costs
- Support for mission-critical business functions

────────────────────────────────────────────────────────────────────────

## 🧩 Architecture Overview

Below is a sanitized architecture diagram representing the capacity optimization workflow:
```
+-----------------------------------------------------------+
|                   ServiceNow Platform                     |
|   (Application Nodes • MID Servers • Integration Layers)  |
+---------------------------+-------------------------------+
                            |
                            v
                +---------------------------+
                |   Capacity Data Sources   |
                | CPU • RAM • Disk • I/O    |
                | Network • JVM • Logs      |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |  Data Collection Scripts  |
                |  Python • PowerShell      |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |  Aggregation & Analysis   |
                |  Forecasting Models       |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |   Recommendations & Ops   |
                |   Scaling • Tuning        |
                +---------------------------+
```

### 📷 Visual Architecture Diagram (PNG)

![Capacity Optimization Architecture](https://github.com/Suren-Jewels/ServiceNow-Capacity-Optimization/blob/main/Capacity_Optimization_Architecture.png?raw=true)

## 🧩 Architecture Layers

| Layer | Purpose | Components |
|-------|----------|------------|
| 🧭 User Interaction Layer | Entry point for all ServiceNow requests and workflows | Service Portal, Catalog Items, Request Forms |
| 🔐 Identity & Access Layer | Validates user identity, RBAC, and SSO attributes | SSO, MFA, IdP, Role Assignments |
| ⚙️ Workflow Automation Layer | Executes approval chains, provisioning logic, and fulfillment tasks | Flow Designer, Workflows, Business Rules |
| 🗄️ Data & Record Layer | Stores request data, audit logs, and configuration items | Tables, CMDB, Audit History |
| 📡 Integration Layer | Connects ServiceNow to external systems and APIs | MID Server, REST APIs, YubiEnterprise API |
| 📊 Monitoring & Compliance Layer | Tracks request status, SLA adherence, and audit requirements | Dashboards, Reports, SLA Engine |

## 📊 Metrics Analyzed

| Metric Type | Parameters | Threshold Analysis |
|-------------|------------|-------------------|
| **💻 Compute** | CPU utilization<br>Core allocation<br>Thread saturation | Peak load identification<br>Bottleneck detection |
| **🧠 Memory** | RAM usage<br>Swap utilization<br>Memory leaks | Capacity planning<br>Resource optimization |
| **💾 Storage** | Disk I/O<br>Storage capacity<br>Read/write patterns | Performance tuning<br>Growth forecasting |
| **🌐 Network** | Bandwidth usage<br>Latency<br>Packet loss | Connectivity health<br>Throughput optimization |
| **☕ Application** | JVM heap<br>Garbage collection<br>Thread pools | Application tuning<br>Performance optimization |

────────────────────────────────────────────────────────────────────────

## 🔐 Authentication Workflow

| Step | Action | Purpose |
|------|--------|----------|
| 1 | User authenticates through SSO with MFA enforced by the identity provider | Ensures secure, verified access to the ServiceNow platform |
| 2 | ServiceNow receives user attributes and roles from the IdP | Establishes RBAC, group membership, and access scope |
| 3 | Platform validates session integrity and user permissions | Confirms the user can access catalog items, dashboards, and workflows |
| 4 | Workflow or catalog request triggers identity‑based logic | Ensures approvals, tasks, and automation follow correct access rules |
| 5 | API calls or MID Server actions authenticate using scoped credentials | Protects integrations and enforces least‑privilege access |
| 6 | Audit logs capture authentication, role evaluation, and workflow execution | Provides traceability for compliance and troubleshooting |
| 7 | Session monitoring evaluates activity, SLA adherence, and anomalies | Supports operational visibility and security posture |

•••••••••••••••

## 📈 Capacity Engineering Workflow

| Step | Action | Tools | Output |
|------|--------|-------|--------|
| **1** | Collect system metrics | 🐍 Python scripts<br>📊 Monitoring APIs | CPU, RAM, I/O, disk, network data |
| **2** | Normalize and aggregate data | 🐍 Python pandas<br>💠 PowerShell | Unified dataset across 1,000+ nodes |
| **3** | Identify bottlenecks | 📊 Analytics tools<br>📈 Visualization | Hotspots, saturation points, underutilized resources |
| **4** | Build capacity models | 🐍 Python modeling<br>📊 Forecasting | Future demand predictions |
| **5** | Recommend scaling actions | 📋 Analysis reports<br>📊 Dashboards | Vertical/horizontal scaling recommendations |
| **6** | Validate improvements | 🧪 Load testing<br>📊 Telemetry | Performance validation metrics |
| **7** | Document and present | 📄 Reports<br>📊 Presentations | Executive summaries and technical docs |

•••••••••••••••

## 🔧 Common Troubleshooting Scenarios

| Issue Type | Symptoms | Resolution |
|------------|----------|------------|
| 🔐 SSO / MFA Failures | User cannot authenticate or is redirected repeatedly | Validate IdP logs, check SSO attributes, confirm MFA enrollment |
| 🧭 Catalog Item Issues | Missing fields, broken forms, or incorrect routing | Review form configuration, UI policies, and workflow bindings |
| ⚙️ Workflow Failures | Approvals not triggering, tasks not generating | Check Flow Designer logs, business rules, and task conditions |
| 🗄️ Data Integrity Problems | Incorrect CI mapping, missing records | Validate CMDB relationships, fix table permissions, re-run discovery |
| 📡 Integration Errors | API calls failing, MID Server offline | Check credentials, API endpoints, MID Server health |
| 📊 SLA / Reporting Gaps | SLAs not updating, dashboards incorrect | Recalculate SLAs, validate report sources, fix time-based conditions |

────────────────────────────────────────────────────────────────────────

## 🚀 Deployment Workflow

**Pipeline:** *[CI] → [CD] → [Prod]*
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

•••••••••••••••

## ✅ Key Outcomes

- **32%** improvement in resource utilization
- **$2M+** recovered from unused hardware and licenses
- Managed **1,000+ servers** across **34 PODs**
- Prevented infrastructure overrun through proactive capacity planning
- Stabilized RHEL8 upgrade path for global teams
- Reduced manual capacity analysis overhead by **60%**

•••••••••••••••

## 🚀 Key Achievements

| Metric | Achievement | Impact |
|--------|-------------|--------|
| 📊 Capacity Forecasting | Built automated ServiceNow capacity models | Prevented outages and improved resource planning |
| 💰 Cost Efficiency | Identified unused or oversized workloads | Reduced operational costs across environments |
| ⚙️ Performance Stability | Tuned platform components for peak load | Improved response times and user experience |
| 🔍 Visibility | Created dashboards for real‑time capacity insights | Enabled proactive decision‑making for operations teams |

•••••••••••••••

## 🧩 Engineering Challenges Solved

- ✅ Identified CPU, memory, and I/O saturation across 1,000+ servers
- ✅ Resolved performance degradation caused by JVM heap exhaustion and GC pressure
- ✅ Normalized inconsistent telemetry data from multiple monitoring systems
- ✅ Automated capacity reporting to eliminate manual analysis overhead
- ✅ Detected underutilized nodes and reduced infrastructure waste
- ✅ Improved forecasting accuracy for peak load periods
- ✅ Strengthened collaboration between SRE, Cloud, and ServiceNow teams
- ✅ Built migration planning logic for server consolidation and scaling

────────────────────────────────────────────────────────────────────────

## 🗂️ Repository Structure
```
ServiceNow-Capacity-Optimization/
│
├── docs/
│   ├── architecture_overview.md        # Sanitized architecture documentation
│   └── confidentiality_note.md         # NDA-aligned disclaimer
│
├── scripts/
│   ├── capacity_analysis.ps1           # PowerShell capacity analysis automation
│   ├── server_migration_plan.sql       # SQL-based migration planning logic
│   └── data_collection.py              # Python metric collector (example)
│
├── Capacity_Optimization_Architecture.png   # Visual architecture diagram
└── README.md                                # This file
```

### 📁 Directory Descriptions

| Directory | Purpose |
|-----------|---------|
| `docs/` | High‑level architecture notes, workflow diagrams, and capacity modeling documentation |
| `dashboards/` | ServiceNow dashboard JSON exports and visualization configurations |
| `scripts/` | Automation tools for data extraction, metric validation, and capacity analysis |
| `reports/` | Sanitized capacity reports, trend summaries, and performance insights |

•••••••••••••••

## 📄 Key Files & Resources

| File | Description |
|------|-------------|
| [architecture_overview.md](https://github.com/Suren-Jewels/ServiceNow-Capacity-Optimization/blob/main/docs/architecture_overview.md) | Detailed system architecture documentation |
| [confidentiality_note.md](https://github.com/Suren-Jewels/ServiceNow-Capacity-Optimization/blob/main/docs/confidentiality_note.md) | NDA compliance and sanitization notice |
| [capacity_analysis.ps1](https://github.com/Suren-Jewels/ServiceNow-Capacity-Optimization/blob/main/scripts/capacity_analysis.ps1) | PowerShell automation for capacity analysis |
| [server_migration_plan.sql](https://github.com/Suren-Jewels/ServiceNow-Capacity-Optimization/blob/main/scripts/server_migration_plan.sql) | Migration planning and consolidation logic |

────────────────────────────────────────────────────────────────────────

## 🔒 Confidentiality Notice

All content is fully sanitized.

No internal ServiceNow data, proprietary dashboards, or sensitive operational details are included.

Only high-level engineering concepts and workflows are described.

## 📄 License

This repository contains sanitized documentation for portfolio purposes only.  
All proprietary information remains confidential per NDA requirements.


# 📊 ServiceNow Capacity Optimization Engine
**Automated analytics, forecasting, and operational insights for mission‑critical ServiceNow environments**

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
- `architecture-summary.md` — high‑level system overview  
- `architecture-layers.md` — functional decomposition  
- `architecture-diagram.md` — sanitized ASCII diagram  

### 🧰 Scripts  
- Metric collectors (Python + PowerShell)  
- API clients  
- Data normalization  
- Forecasting engine  
- Capacity analysis utilities  
- End‑to‑end job runner  

### ⚙ Configuration  
- `baseline-config.json` — core settings and API endpoints  
- `environment-profile.yaml` — environment‑specific overrides  

---

## 🚀 Deployment Workflow  
1. Prepare environment and credentials  
2. Configure API endpoints and thresholds  
3. Run collectors to gather raw metrics  
4. Normalize data for analytics  
5. Generate capacity forecasts  
6. Validate outputs and dashboards  
7. Schedule recurring automation  

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
This repository demonstrates engineering capability in automation, analytics, and platform reliability — aligned with enterprise ServiceNow operations and mission‑critical system performance.

