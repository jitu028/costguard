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
🚀 Quickstart
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/<your-username>/costguard.git
cd costguard
2. Create and activate a virtual environment
bash
Copy
Edit
python3 -m venv .adk-venv
source .adk-venv/bin/activate
3. Install dependencies using Poetry
bash
Copy
Edit
poetry install --with deployment
4. Configure your .env file
dotenv
Copy
Edit
GCP_PROJECT=your-gcp-project-id
GCP_LOCATION=us-central1
GCP_BUCKET=your-gcs-staging-bucket
BQ_DATASET=your_bq_dataset
BQ_TABLE=your_bq_export_table
5. Deploy the agent to Vertex AI
bash
Copy
Edit
python deployment/deploy.py --create
💬 Example Queries
Try natural language prompts like:

“Give me a cost summary for the last 30 days.”

“Which GCP project has exceeded its budget this month?”

“How can we optimize our Compute Engine usage?”

🧪 Run Tests
bash
Copy
Edit
pytest tests/
pytest eval/
📈 Roadmap
 Cost summary retrieval via BigQuery

 Budget alert detection agent

 Static recommendations engine

 Dynamic usage pattern analysis

 Real-time anomaly detection

 Slack/Gmail notification integration

 Multi-agent approval workflows

🔐 Required IAM Permissions
Ensure the execution environment's service account has:

bigquery.jobs.create

bigquery.readsessions.create

aiplatform.models.predict

storage.objectViewer (optional for GCS logs or staging)

🤝 Contributing
We welcome PRs, issues, and ideas! To contribute:

Fork the repo

Create a feature branch

Submit a pull request

📄 License
Licensed under the Apache 2.0 License.

👤 Author
Jitendra Gupta
Google Cloud Architect | GDE | Community Mentor
🔗 LinkedIn
✍️ Medium Articles

Cloud FinOps, now AI-native — with CostGuard.

yaml
Copy
Edit

---

Let me know if you'd like:
- a `CONTRIBUTING.md` guide
- Markdown badges (e.g. version, license, build)
- Example screenshots or GIFs of usage (CLI or web UI)
