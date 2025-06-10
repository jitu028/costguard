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



Let me know if you'd like:
- a `CONTRIBUTING.md` guide
- Markdown badges (e.g. version, license, build)
- Example screenshots or GIFs of usage (CLI or web UI)
