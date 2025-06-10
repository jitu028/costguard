"""BigQuery utility functions for CostGuard agent"""

import os
from typing import Optional
from dotenv import load_dotenv

from google.cloud import bigquery

# Load environment variables from .env file
load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT")
DATASET = os.getenv("BQ_DATASET")
TABLE = os.getenv("BQ_TABLE")

client = bigquery.Client(project=PROJECT_ID)


def run_dynamic_query(sql_template: str, **params) -> str:
    """Generic function to safely format and run a parameterized BigQuery SQL."""
    try:
        query = sql_template.format(PROJECT_ID=PROJECT_ID, DATASET=DATASET, TABLE=TABLE, **params)
        result = client.query(query).result()
        rows = [row for row in result]
        if not rows:
            return "No data found."

        # Format to markdown table
        headers = rows[0].keys()
        table = "| " + " | ".join(headers) + " |\n"
        table += "|" + "|".join(["---"] * len(headers)) + "|\n"
        for row in rows:
            table += "| " + " | ".join([str(row[field]) if row[field] is not None else "N/A" for field in headers]) + " |\n"
        return table
    except Exception as e:
        return f"Error: {str(e)}"


def get_cost_summary(days: Optional[int]) -> str:
    '''Function to get cost summary for the past `days` number of days.'''
    sql = """
    SELECT
      service.description AS service,
      project.id AS project_id,
      ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL {days} DAY)
    GROUP BY service, project_id
    ORDER BY total_cost DESC
    LIMIT 10
    """
    return run_dynamic_query(sql, days=days)


def get_total_spend() -> str:
    """Function to get the total spend across all projects."""
    sql = """
    SELECT ROUND(SUM(cost), 2) AS total_spend
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    """
    return run_dynamic_query(sql)


def get_high_cost_projects(limit: int = 5) -> str:
    """Function to get the top N projects by total cost."""
    sql = """
    SELECT project.id AS project_id, ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY project_id
    ORDER BY total_cost DESC
    LIMIT {limit}
    """
    return run_dynamic_query(sql, limit=limit)


def get_cost_by_region() -> str:
    """Function to get total cost by region."""
    sql = """
    SELECT location.location AS region, ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY region
    ORDER BY total_cost DESC
    """
    return run_dynamic_query(sql)


def get_daily_spend_trend(days: int) -> str:
    """Function to get daily spend trend for the past `days` number of days."""
    sql = """
    SELECT DATE(usage_start_time) AS usage_date, ROUND(SUM(cost), 2) AS daily_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL {days} DAY)
    GROUP BY usage_date
    ORDER BY usage_date
    """
    return run_dynamic_query(sql, days=days)


def get_cost_by_service() -> str:
    """Function to get total cost by service."""
    sql = """
    SELECT service.description AS service, ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY service
    ORDER BY total_cost DESC
    LIMIT 10
    """
    return run_dynamic_query(sql)


def get_cost_by_label(label_key: str) -> str:
    """Function to get total cost by a specific label key."""
    sql = f"""
    SELECT labels.{label_key} AS label_value, ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY label_value
    ORDER BY total_cost DESC
    """
    return run_dynamic_query(sql)


def get_monthly_spend_by_project() -> str:
    """Function to get monthly spend by project."""
    sql = """
    SELECT
      FORMAT_TIMESTAMP('%Y-%m', usage_start_time) AS month,
      project.id AS project_id,
      ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY month, project_id
    ORDER BY month DESC, total_cost DESC
    """
    return run_dynamic_query(sql)


def get_services_exceeding_threshold(threshold: float) -> str:
    """Function to get services with total cost exceeding a specified threshold."""
    sql = """
    SELECT service.description AS service, ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY service
    HAVING total_cost > {threshold}
    ORDER BY total_cost DESC
    """
    return run_dynamic_query(sql, threshold=threshold)


def get_cost_variance_by_week() -> str:
    """Function to get cost variance by week."""
    sql = """
    SELECT
      FORMAT_TIMESTAMP('%Y-%W', usage_start_time) AS week,
      ROUND(SUM(cost), 2) AS total_cost
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY week
    ORDER BY week DESC
    """
    return run_dynamic_query(sql)


def get_recommendations_mock() -> str:
    """Mock function to return recommendations for cost optimization."""
    return "\n".join([
        "- **Idle VMs Detected**: Several VMs have <5% CPU usage over the past month. Consider stopping them.",
        "- **Committed Use Discounts**: Eligible for CUDs in `us-central1` on Compute Engine.",
        "- **BigQuery Slots**: Auto-scaling option not enabled. Consider switching from flat-rate pricing."
    ])
