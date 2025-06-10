# CostGuard — GCP FinOps AI Agent 🤖💰

**CostGuard** is an intelligent, multi-tool AI agent built using [Google’s Agent Development Kit (ADK)](https://cloud.google.com/vertex-ai/docs/agent-builder/adk/overview). It empowers FinOps and CloudOps teams with real-time visibility into Google Cloud costs, detects budget anomalies, and suggests actionable cloud optimization strategies.

---

## 🔍 Why CostGuard?

Managing GCP cloud spend can be complex and reactive. CostGuard enables:

- ✅ Real-time **cost summaries**
- ✅ Detection of **budget threshold breaches**
- ✅ **Cloud savings recommendations**
- ✅ Natural language interactions with Gemini models
- ✅ Extensible multi-agent orchestration with tools

---

## 📦 Project Structure

```bash
costguard/
├── shared_libraries/              # Reusable components (constants, BigQuery utils)
│   ├── constants.py
│   └── bigquery_utils.py
│
├── sub_agents/                    # Modular sub-agents for FinOps functions
│   ├── budget_alert/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── prompt.py
│   ├── cost_summary/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── prompt.py
│   └── recommendations/
│       ├── __init__.py
│       ├── agent.py
│       └── prompt.py
│
├── tools/                         # Additional prompt or agent utilities
│   ├── __init__.py
│   ├── agent.py
│   └── prompt.py
│
├── deployment/                    # Scripts for deployment to Vertex AI
│   ├── deploy.py
│   └── test_deployment.py
│
├── eval/                          # Evaluation test data and scripts
│   ├── test_eval.py
│   └── data/
│       └── cost_sage_evalset.test.json
│
├── tests/                         # Pytest test cases
│   └── test_agents.py
│
├── costguard/                     # Root agent definition
│   ├── __init__.py
│   ├── agent.py
│   └── prompt.py
│
├── .env                           # GCP credentials and configuration
├── README.md
├── pyproject.toml                 # Poetry dependency and project config
└── poetry.lock


---

git clone https://github.com/<your-username>/costguard.git
cd costguard

python3 -m venv .adk-venv
source .adk-venv/bin/activate

poetry install --with deployment

GCP_PROJECT=your-gcp-project-id
GCP_LOCATION=us-central1
GCP_BUCKET=your-gcs-staging-bucket
BQ_DATASET=your_bq_dataset
BQ_TABLE=your_bq_export_table

python deployment/deploy.py --create


