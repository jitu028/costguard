# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
