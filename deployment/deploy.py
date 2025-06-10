
"""Deployment script for CostGuard agent."""

import os

import vertexai
from absl import app, flags
from dotenv import load_dotenv

from costguard.agent import root_agent

from costguard.shared_libraries import constants

from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp

# This script deploys the CostGuard agent to Google Cloud Vertex AI.


FLAGS = flags.FLAGS
flags.DEFINE_string("project_id", None, "GCP project ID.")
flags.DEFINE_string("location", None, "GCP location.")
flags.DEFINE_string("bucket", None, "GCP bucket.")
flags.DEFINE_string("resource_id", None, "ReasoningEngine resource ID.")
flags.DEFINE_bool("list", False, "List all agents.")
flags.DEFINE_bool("create", False, "Creates a new agent.")
flags.DEFINE_bool("delete", False, "Deletes an existing agent.")
flags.mark_bool_flags_as_mutual_exclusive(["create", "delete"])


def create() -> None:
    """Creates a new remote agent using the AdkApp template."""
    adk_app = AdkApp(agent=root_agent, enable_tracing=True)
    extra_packages = ["./costguard"]

    remote_agent = agent_engines.create(
        adk_app,
        requirements=[
            "google-adk (>=1.0.0,<2.0.0)",
            "google-cloud-aiplatform[agent_engines] (>=1.93.0)",
            "google-genai (>=1.5.0,<2.0.0)",
            "pydantic (>=2.10.6,<3.0.0)",
            "absl-py (>=2.2.1,<3.0.0)",
            "python-dotenv",
            "google-cloud-bigquery",
        ],
        extra_packages=extra_packages,
    )
    print(f"Created remote agent: {remote_agent.resource_name}")


def delete(resource_id: str) -> None:
    """Deletes an existing remote agent by resource ID."""
    remote_agent = agent_engines.get(resource_id)
    remote_agent.delete(force=True)
    print(f"Deleted remote agent: {resource_id}")


def list_agents() -> None:
    """Lists all remote agents."""
    remote_agents = agent_engines.list()
    template = """
{agent.name} ("{agent.display_name}")
- Create time: {agent.create_time}
- Update time: {agent.update_time}
"""
    remote_agents_string = "\n".join(
        template.format(agent=agent) for agent in remote_agents
    )
    print(f"All remote agents:\n{remote_agents_string}")


def main(argv: list[str]) -> None:
    """Main function to handle command line arguments and execute actions."""
    del argv  # unused
    project_id = FLAGS.project_id if FLAGS.project_id else constants.PROJECT
    location = FLAGS.location if FLAGS.location else constants.LOCATION
    bucket = FLAGS.bucket if FLAGS.bucket else constants.STAGING_BUCKET
    
    load_dotenv()

    project_id = (
        FLAGS.project_id if FLAGS.project_id else os.getenv("GCP_PROJECT")
    )
    location = (
        FLAGS.location if FLAGS.location else os.getenv("LOCATION")
    )
    bucket = (
        FLAGS.bucket if FLAGS.bucket else os.getenv("STORAGE_BUCKET")
    )

    print(f"PROJECT: {project_id}")
    print(f"LOCATION: {location}")
    print(f"BUCKET: {bucket}")

    if not project_id:
        print("Missing required environment variable: GOOGLE_CLOUD_PROJECT")
        return
    elif not location:
        print("Missing required environment variable: GOOGLE_CLOUD_LOCATION")
        return
    elif not bucket:
        print("Missing required environment variable: STORAGE_BUCKET")
        return

    vertexai.init(
        project=project_id,
        location=location,
        staging_bucket=f"gs://{bucket}",
    )

    if FLAGS.list:
        list_agents()
    elif FLAGS.create:
        create()
    elif FLAGS.delete:
        if not FLAGS.resource_id:
            print("resource_id is required for delete")
            return
        delete(FLAGS.resource_id)
    else:
        print("Unknown command")


if __name__ == "__main__":
    app.run(main)
