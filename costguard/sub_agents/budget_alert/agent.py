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

"""CostGuard sub-agents package initializer."""


from google.adk.agents.llm_agent import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

budget_alert_agent = Agent(
    model=MODEL,
    name="budget_alert_agent",
    instruction=prompt.BUDGET_ALERT_PROMPT,
)
