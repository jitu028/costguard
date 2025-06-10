"""Recommendations sub-agent for costguard."""


from google.adk import Agent

from costguard.tools import bigquery_utils


from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

recommendations_agent = Agent(
    model=MODEL,
    name="recommendations_agent",
    instruction=prompt.RECOMMENDATIONS_PROMPT,
    tools=[
        bigquery_utils.get_recommendations_mock,
    ],
)
