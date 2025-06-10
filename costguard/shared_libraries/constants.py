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

"""Defines constants."""

import os
import dotenv

dotenv.load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.5-pro-preview-05-06")
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "gcp-demo-028")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
STAGING_BUCKET = os.getenv("STAGING_BUCKET", "gcp-demo-028-agents")
DATASET_ID = os.getenv("DATASET_ID", "cloudexporthub")
TABLE_ID = os.getenv("TABLE_ID", "gcp_billing_export_resource_v1_010040_690C15_CB3933")
AGENT_NAME = "costguard_agent"
DESCRIPTION = "Monitors GCP spending, evaluates budgets, and suggests \
        cloud cost savings."
