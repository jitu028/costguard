
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
