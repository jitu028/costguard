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

"""Test cases for the CostGuard Agent."""

import textwrap
import dotenv
import pytest
from google.adk.runners import InMemoryRunner
from google.genai.types import Part, UserContent
from ...costguard.agent import root_agent

pytest_plugins = ("pytest_asyncio",)


@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Load environment variables from .env file for the test session."""
    dotenv.load_dotenv()


@pytest.mark.asyncio
async def test_cost_summary_query():
    """Runs agent with GCP cost-related query & expects a response."""
    user_input = textwrap.dedent(
        """
        Can you provide a cost summary for the last 7 days?
        """
    ).strip()

    runner = InMemoryRunner(agent=root_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="test_user"
    )
    content = UserContent(parts=[Part(text=user_input)])
    response = ""

    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        if event.content.parts and event.content.parts[0].text:
            response = event.content.parts[0].text
            print(response)

    assert "project" in response.lower() or "cost" in response.lower()
