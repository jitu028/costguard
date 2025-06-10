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
