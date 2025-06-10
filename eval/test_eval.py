import pytest
from costguard.agent import costguard_agent


@pytest.mark.parametrize(
    "query",
    [
        "Give me a cost summary for the last 30 days",
        "Have we crossed our budget on any project?",
        "How can we reduce our GCP bill this month?",
    ],
)
def test_agent_responds(query):
    response = costguard_agent.run_sync(query)
    assert response and len(response.text) > 10
