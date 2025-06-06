import os
import sys

import vertexai
from dotenv import load_dotenv
from vertexai.preview import reasoning_engines

from service_coordinator_agent.agent import root_agent


def main():
    # Load environment variables
    load_dotenv()

    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_LOCATION")
    bucket = os.getenv("GOOGLE_CLOUD_STAGING_BUCKET")


    if not project_id:
        print("Missing required environment variable: GOOGLE_CLOUD_PROJECT")
        sys.exit(1)
    elif not location:
        print("Missing required environment variable: GOOGLE_CLOUD_LOCATION")
        sys.exit(1)

    # Initialize Vertex AI
    print(f"Initializing Vertex AI with project local={project_id}, location={location}, bucket= {bucket}")
    vertexai.init(
        project=project_id,
        location=location,
    )
    initial_state = {
    "user_name": "IKEA Customer",
    "cart_details": [
        {
            "name": "Kallax Shelf Unit",
            "sku": "FURN-001",
            "id": "00263850",
            "quantity": 1,
            "itemType": "ART",
            "price": 79.99
        },
        {
            "name": "Kitchen Cabinet Base",
            "sku": "KIT-005",
            "id": "50263838",
            "quantity": 2,
            "itemType": "ART",
            "price": 199.99
        }
    ],
    "interaction_history": []
    }

    # Create the app
    print("Creating local app instance...")
    app = reasoning_engines.AdkApp(
        agent=root_agent,
        enable_tracing=False,
    )

    # Create a session
    print("Creating session...")
    session = app.create_session(user_id="test_user", state=initial_state)
    print("Session created:")
    print(f"  Session ID: {session.id}")
    print(f"  User ID: {session.user_id}")
    print(f"  App name: {session.app_name}")

    # List sessions
    print("\nListing sessions...")
    sessions = app.list_sessions(user_id="test_user")
    if hasattr(sessions, "sessions"):
        print(f"Found sessions: {sessions.sessions}")
    elif hasattr(sessions, "session_ids"):
        print(f"Found session IDs: {sessions.session_ids}")
    else:
        print(f"Sessions response: {sessions}")

    # Send a test query
    print("\nSending test query...")
    test_message = (
        "Hello, how are you doing today? I hope you're having a wonderful day!"
    )
    print(f"Message: {test_message}")
    print("\nResponse:")
    for event in app.stream_query(
        user_id="test_user",
        session_id=session.id,
        message=test_message,
    ):
        print(event)


if __name__ == "__main__":
    main()