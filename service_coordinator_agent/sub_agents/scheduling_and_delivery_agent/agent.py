from google.adk.agents import Agent
import google.adk.tools.tool_context as ToolContext
import requests

import random
from typing import Optional, List, Dict
from pydantic import BaseModel

# Simulated persistent state for interaction
interaction_state = {
    "available_dates": [],
    "available_times": [],
    "confirmed": False
}

# Define Input Schema
class SchedulingInput(BaseModel):
    selected_date: Optional[str] = None
    selected_time: Optional[str] = None

# Define Output Schema
class SchedulingOutput(BaseModel):
    available_dates: Optional[List[str]] = None
    available_times: Optional[List[str]] = None
    confirmed_date: Optional[str] = None
    confirmed_time: Optional[str] = None
    delivery_mode: Optional[str] = None
    message: str

# Refactored Function (no longer takes ToolContext directly)
def scheduling_tool(tool_context: ToolContext, selected_date: Optional[str]= None, selected_time: Optional[str]= None) -> SchedulingOutput:
    """
    Determines available delivery dates and times for the services based on the items in the cart.
    Also determines the best possible service date and delivery mode.
    Args:
        tool_context (ToolContext): The context containing the current state and cart details.
        selected_date (str): The date selected by the user for delivery.
        selected_time (str): The time selected by the user for delivery.
    Returns:
        SchedulingOutput: Includes available dates and times, confirmed date and time, delivery mode, and a message.
    """
    # Get current cart 
    cart_details = tool_context.state.get("cart_details", [])
    if not cart_details:
        return SchedulingOutput(message="No items found in the cart.")

    # Step 1: Present options if not already stored
    if not interaction_state["available_dates"]:
        available_dates = [f"2025-10-{str(day).zfill(2)}" for day in range(1, 11)]
        available_times = [
            "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
            "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM",
            "05:00 PM", "06:00 PM"
        ]

        interaction_state["available_dates"] = available_dates
        interaction_state["available_times"] = available_times

        return SchedulingOutput(
            available_dates=available_dates,
            available_times=available_times,
            message="Please select a date and time from the available options and call the tool again with those selected values."
        )

    # Step 2: Confirm selected slot
    if selected_date and selected_time:
        if selected_date not in interaction_state["available_dates"]:
            return SchedulingOutput(message=f"{selected_date} is not in available dates.")
        if selected_time not in interaction_state["available_times"]:
            return SchedulingOutput(message=f"{selected_time} is not in available times.")

        total_cart_value = sum(item.get("price", 0) for item in cart_details)
        item_count = len(cart_details)

        if item_count >= 5 or total_cart_value > 1000:
            delivery_mode = "Scheduled Delivery"
        elif total_cart_value > 200:
            delivery_mode = "Express Delivery"
        else:
            delivery_mode = "Standard Delivery"

        interaction_state["confirmed"] = True
        print(f"Scheduling confirmed for {selected_date} at {selected_time} with delivery mode: {delivery_mode}")
        res = SchedulingOutput(
            confirmed_date=selected_date,
            confirmed_time=selected_time,
            delivery_mode=delivery_mode,
            message=f"Delivery scheduled on {selected_date} at {selected_time} via {delivery_mode}."
        )
        print(f"Scheduling output: {res}")
        return SchedulingOutput(
            confirmed_date=selected_date,
            confirmed_time=selected_time,
            delivery_mode=delivery_mode,
            message=f"Delivery scheduled on {selected_date} at {selected_time} via {delivery_mode}."
        )

    return SchedulingOutput(message="Please provide both selected_date and selected_time to confirm scheduling.")

scheduling_and_delivery_agent = Agent(
    name="scheduling_and_delivery_agent",
    model="gemini-2.0-flash",
    description="This agent schedules services for the items in the cart based on the analysis provided by the service_matcher_agent.",
    instruction="""
        You are a service scheduling agent for IKEA customers.
        Your task is to help schedule services related to products in the user's cart.

        Workflow:
        1. Retrieve items in the user's cart from the tool context.
        2. Use the `scheduling_tool` to present available delivery dates and times.
        3. Ask the user to choose a preferred delivery slot interactively.
        4. Accept user input for the selected date and time
        5. On receiving the user's selection, call the `scheduling_tool` again with the selected date and time to confirm the delivery and determine the delivery mode.

        Important:
        - Do not guess or fabricate services.
        - Only use the `scheduling_tool` to determine available and confirmed delivery slots.
        - If the user has not yet selected a slot, prompt them using the output of `scheduling_tool`.
        - Handle inputs interactively via the tool context (`tool_conte
        """,
    sub_agents=[],
    tools=[scheduling_tool]
)