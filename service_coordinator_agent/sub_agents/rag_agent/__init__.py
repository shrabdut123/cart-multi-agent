"""
Vertex AI RAG Agent

A package for interacting with Google Cloud Vertex AI RAG capabilities.
"""

import os

import vertexai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Vertex AI configuration from environment
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
bucket = os.environ.get("GOOGLE_CLOUD_STAGING_BUCKET")

# Initialize Vertex AI at package load time
try:
    if PROJECT_ID and LOCATION:
        print(f"Initializing Vertex AI with project init={PROJECT_ID}, location={LOCATION}, bucket={bucket}")
        vertexai.init(project=PROJECT_ID, location=LOCATION)
        print("Vertex AI initialization successful")
    else:
        print(
            f"Missing Vertex AI configuration. PROJECT_ID={PROJECT_ID}, LOCATION={LOCATION}. "
            f"Tools requiring Vertex AI may not work properly."
        )
except Exception as e:
    print(f"Failed to initialize Vertex AI: {str(e)}")
    print("Please check your Google Cloud credentials and project settings.")

# Import agent after initialization is complete
from . import agent