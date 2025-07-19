"""Cost summary sub-agent for costguard."""

from google.adk import Agent

from costguard.tools import bigquery_utils

from . import prompt


MODEL = "gemini-2.5-pro-preview-05-06"

cost_summary_agent = Agent(
    model=MODEL,
    name="cost_summary_agent",
    instruction=prompt.COST_SUMMARY_PROMPT,
    tools=[
        bigquery_utils.get_cost_summary,
        bigquery_utils.get_total_spend,
        bigquery_utils.get_high_cost_projects,
        bigquery_utils.get_cost_by_region,
        bigquery_utils.get_daily_spend_trend,
        bigquery_utils.get_cost_by_service,
        bigquery_utils.get_cost_by_label,
        bigquery_utils.get_monthly_spend_by_project,
        bigquery_utils.get_services_exceeding_threshold,
        bigquery_utils.get_cost_variance_by_week,
    ],
)
