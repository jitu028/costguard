"""CostGuard: FinOps agent for GCP cost analysis, budget monitoring,
and savings recommendations."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool


from . import prompt
from .sub_agents.cost_summary.agent import cost_summary_agent
from .sub_agents.budget_alert.agent import budget_alert_agent
from .sub_agents.recommendations.agent import recommendations_agent

MODEL = "gemini-2.5-pro-preview-05-06"

costguard_agent = Agent(
    name="costguard_agent",
    model=MODEL,
    description="Monitors GCP spending, evaluates budgets, and suggests \
        cloud cost savings.",
    instruction=prompt.ROOT_PROMPT,
    output_key="costguard_output",
    tools=[
        AgentTool(agent=cost_summary_agent),
        AgentTool(agent=budget_alert_agent),
        AgentTool(agent=recommendations_agent),
    ],)

root_agent = costguard_agent
