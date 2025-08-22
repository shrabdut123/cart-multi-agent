
# agent.py
import asyncio
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from service_coordinator_agent.utils import add_user_query_to_history, call_agent_async

# Import sub-agents
from .sub_agents.cart_analyzer_agent.agent import cart_analyzer_agent
from .sub_agents.service_matcher_agent.agent import service_matcher_agent
from .sub_agents.upsell_recommender_agent.agent import upsell_recommender_agent
from .sub_agents.rag_agent.agent import rag_agent
from .sub_agents.scheduling_and_delivery_agent.agent import scheduling_and_delivery_agent
from .sub_agents.optimizer_agent.agent import optimizer_agent

# ==============================
# Main Root Agent Definition
# ==============================

# This is the main agent that coordinates the execution of multiple service agents.
root_agent = Agent(
    name="service_coordinator_agent",
    model="gemini-2.0-flash",
    description="This agent coordinates the execution of multiple service agents.",
    instruction="""
    “You are an intelligent assistant at IKEA checkout. Your task is to find out if the current cart has service-eligible items,
    recommend those services, and ensure the customer understands how to proceed.Your tasks include:
    1. Coordinating the execution of service agents.
    2. Ensuring that each service agent completes its task successfully.
    3. Handling any errors or issues that arise during the execution of service agents.
    4. Reporting the status of each service agent to the user.
    5. Providing a summary of the overall execution process.
    6. Logging any relevant information for debugging purposes.
    7. Communicating with other agents as needed to facilitate the execution of tasks.
    8. Ensuring that the execution of service agents is efficient and effective.
    9. Maintaining a record of the execution history for future reference.

    You have access to the following sub-agents:
    - cart_analyzer_agent: Analyzes the cart to determine if the cart contains service-eligible items.
    - service_matcher_agent: Matches services to items in the cart based on eligibility.
    - rag_agent: Provides additional information from the knowledge corpus base to assist in service recommendations.
    - upsell_recommender_agent: Recommends additional services based on the customer's cart and preferences.
    - scheduling_and_delivery_agent: Schedules services for the items in the cart based on the analysis provided by the service_matcher_agent.
                                    Interacts with the user in two phases:First, presents available delivery dates and time slots using the `scheduling_tool`.
                                    Then, waits for the user to select a preferred slot (date and time).On confirmation, the sub-agent returns the scheduled date, time, and appropriate delivery mode based on cart contents.
    -optimizer_agent: Optimizes the cart by suggesting additional items or services that complement the existing products to enhance the overall cart value and customer satisfaction.
    You will use these sub-agents to complete the tasks assigned to you.
    You will not use any tools directly, but will rely on the sub-agents to perform the necessary actions.
    You will ensure that the execution of service agents is efficient and effective, and that the customer understands how to proceed with the services.
        """,
    sub_agents=[cart_analyzer_agent, service_matcher_agent, rag_agent, upsell_recommender_agent, scheduling_and_delivery_agent , optimizer_agent],

    tools=[],
)

# ==============================
# Optional CLI Runner Entry Point
# ==============================

def start_interactive_session():
    asyncio.run(_main_async())

async def _main_async():
    load_dotenv()
    session_service = InMemorySessionService()
    print("Initializing session service..********************.")
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
            }
        ],
        "interaction_history": []
    }

    APP_NAME = "IKEA Support"
    USER_ID = "aiwithshrabani"

    new_session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state
    )
    SESSION_ID = new_session.id

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    print("\nWelcome to Customer Service Chat!")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Goodbye!")
            break

        add_user_query_to_history(
            session_service, APP_NAME, USER_ID, SESSION_ID, user_input
        )

        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)

    final_session = session_service.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    print("\nFinal Session State:")
    for key, value in final_session.state.items():
        print(f"{key}: {value}")

# Only run if this script is executed directly
if __name__ == "__main__":
    start_interactive_session()