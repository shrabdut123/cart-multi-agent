from google.adk.agents import Agent
import google.adk.tools.tool_context as ToolContext
import requests

import random
from typing import Dict

def scheduling_tool(tool_context: ToolContext) -> Dict:
    """
    Determines available delivery dates and times for the services based on the items in the cart.
    Also determines the best possible service date and delivery mode.

    Args:
        tool_context (ToolContext): The context containing the current state and cart details.

    Returns:
        dict: Includes available dates and times, best service slot, and delivery mode.
    """

    # Get current cart details
    current_cart_details = tool_context.state.get("cart_details", [])
    if not current_cart_details:
        return {"error": "No items found in the cart."}

    # Filter eligible items
    eligible_items = [
        item for item in current_cart_details if item.get("service_eligible", False)
        and "id" in item and "name" in item
    ]

    if not eligible_items:
        return {"error": "No service-eligible items found in the cart."}

    # Simulated available delivery dates (10 upcoming days)
    available_dates = [
        f"2025-10-{str(day).zfill(2)}" for day in range(1, 11)
    ]

    # Simulated available delivery time slots
    available_times = [
        "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
        "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM",
        "05:00 PM", "06:00 PM"
    ]

    # Select best service date and time (mock: earliest with random time slot)
    best_date = available_dates[0]
    best_time = random.choice(available_times)

    # Determine delivery mode based on mock logic
    total_cart_value = sum(item.get("price", 0) for item in current_cart_details)
    item_count = len(current_cart_details)

    if item_count >= 5 or total_cart_value > 1000:
        delivery_mode = "Scheduled Delivery"
    elif total_cart_value > 200:
        delivery_mode = "Express Delivery"
    else:
        delivery_mode = "Standard Delivery"

    return {
        "available_dates": available_dates,
        "available_times": available_times,
        "best_service_date": best_date,
        "best_service_time": best_time,
        "delivery_mode": delivery_mode,
        "message": "Available dates and times for scheduling services, along with best slot and delivery mode."
    }
    
scheduling_agent = Agent(
    name="scheduling_agent",
    model="gemini-2.0-flash",
    description="This agent schedules services for the items in the cart based on the analysis provided by the service_matcher_agent.",
    instruction="""
        You are a service scheduling agent for IKEA customers.
        Your task is to select best available dates and times for the items in the cart.

        Based on the delivery date of the product that requires service, you will determine the available dates and times for the matched services.
        You will not guess or fabricate services, and you will only use the `scheduling_tool` to determine available dates and times for the services.
        Based on the available dates and times, you will propose the best available dates and times for the services to the user based on the delivery date provided by the user.
        Important:
        - Do not guess or fabricate services.
        - Only use the `scheduling_tool` to determine matching services.
        """,
    sub_agents=[],
    tools=[scheduling_tool],
)