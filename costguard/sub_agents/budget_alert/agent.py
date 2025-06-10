"""CostGuard sub-agents package initializer."""


from google.adk.agents.llm_agent import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

budget_alert_agent = Agent(
    model=MODEL,
    name="budget_alert_agent",
    instruction=prompt.BUDGET_ALERT_PROMPT,
)
