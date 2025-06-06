import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from service_coordinator_agent.agent import root_agent
from utils import add_user_query_to_history, call_agent_async

load_dotenv()

# ===== PART 1: Initialize In-Memory Session Service =====
# Using in-memory storage for this example (non-persistent)
session_service = InMemorySessionService()

# ===== PART 2: Define Initial State =====
# This will be used when creating a new session
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
        },
        {
            "name": "Platsa Wardrobe Frame",
            "sku": "FURN-003",
            "id": "40395245",
            "quantity": 1,
            "itemType": "ART",
            "price": 120.00
        },
        {
            "name": "Office Chair Markus",
            "sku": "FURN-002",
            "id": "50481469",
            "quantity": 1,
            "itemType": "ART",
            "price": 199.99
        },
        {
            "name": "LED Lightbulb E27 400lm",
            "sku": "ACC-004",
            "id": "90395243",
            "quantity": 4,
            "itemType": "ART",
            "price": 9.99
        },
        {
            "name": "LACK Wall Shelf",
            "sku": "FURN-006",
            "id": "60481647",
            "quantity": 2,
            "itemType": "ART",
            "price": 19.99
        },
    ],
    "interaction_history": []
}

async def main_async():
    """Main asynchronous function to run the IKEA support agent."""
    # Create a new session with the initial state
    # Setup constants
    APP_NAME = "IKEA Support"
    USER_ID = "aiwithshrabani"
    # ===== PART 3: Session Creation =====
    # Create a new session with initial state
    new_session =  session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state
    )
    SESSION_ID = new_session.id
    # ===== PART 4: Agent Runner Setup =====
    # Create a runner with the main customer service agent
    
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
      # ===== PART 5: Interactive Conversation Loop =====
    print("\nWelcome to Customer Service Chat!")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Goodbye!")
            break

        # Update interaction history with the user's query
        add_user_query_to_history(
            session_service, APP_NAME, USER_ID, SESSION_ID, user_input
        )

        # Process the user query through the agent
        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

    # ===== PART 6: State Examination =====
    # Show final session state
    final_session = session_service.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    print("\nFinal Session State:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")

def main():
    """Entry point for the application."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
