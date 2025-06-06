from google.adk.agents import Agent

def confirmation_tool(service_quote: dict) -> dict:
    """
    Prepares a confirmation summary based on the service quote and prompts user for final approval.

    Args:
        service_quote (dict): Quote and schedule output including:
            - location: str
            - total_estimated_price: float
            - total_estimated_time_hrs: float
            - service_quote_details: list of items with services info

    Returns:
        dict: Confirmation summary with items, services, total cost, and confirmation prompt.
    """
    items_summary = []
    for item in service_quote.get("service_quote_details", []):
        services = item.get("services", [])
        if services:
            service_lines = [
                f"- {srv['type']} (₹{srv['estimated_price']}, ~{srv['estimated_time_hrs']} hrs)"
                for srv in services
            ]
            items_summary.append(f"📦 **{item['name']}**\n" + "\n".join(service_lines))

    full_summary = "\n\n".join(items_summary)
    total_price = service_quote.get("total_estimated_price", 0)
    total_time = service_quote.get("total_estimated_time_hrs", 0)
    location = service_quote.get("location", "your area")

    confirmation_prompt = (
        f"🛠️ **Service Summary for your order in {location}**:\n\n"
        f"{full_summary}\n\n"
        f"💰 **Total Price**: ₹{total_price}\n"
        f"⏳ **Estimated Time**: {total_time} hrs\n\n"
        "Would you like to confirm and add these services to your order? (yes/no)"
    )

    return {
        "confirmation_summary": confirmation_prompt,
        "pending_confirmation": True
    }

confirmation_agent = Agent(
    name="confirmation_agent",
    model="gemini-2.0-flash",
    description="This agent confirms the execution of service agents and ensures the customer understands how to proceed.",
    instruction="""
    You are an intelligent assistant at IKEA checkout. Your task is to confirm the execution of service agents and ensure the customer understands how to proceed.
    Your tasks include:
    1. Confirming the execution of service agents.
    2. Ensuring that the customer understands how to proceed with the services.
    3. Providing a summary of the overall execution process.
    4. Logging any relevant information for debugging purposes.
    5. Communicating with other agents as needed to facilitate the execution of tasks.
        """,
    sub_agents =[],
    tools=[confirmation_tool],
)