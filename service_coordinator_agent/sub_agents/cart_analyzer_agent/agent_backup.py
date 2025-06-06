from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


import requests

def batch_check_service_eligibility(cart_items):
    url = 'https://service-offers-stage-o2jblwt7ia-ew.a.run.app/graphql'
    headers = {'content-type': 'application/json'}

    # Extract ids from cart items
    ids = [item.get("id") for item in cart_items if "id" in item]

    query = """
    query Query($retailId: String!, $items: [String!]) {
      serviceAvailability(retailId: $retailId) {
        SGR50000960(items: $items) {
          available
          items {
            available
          }
        }
      }
    }
    """

    variables = {
        "retailId": "SE",
        "items": ids
    }

    response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()

    # Defensive parsing of response
    try:
        service_data = data["data"]["serviceAvailability"]["SGR50000960"]
        overall_available = service_data["available"]  # overall availability for the batch
        per_item_availability = service_data.get("items", [])
    except (KeyError, TypeError):
        per_item_availability = []

    # Map each id to its availability (default False)
    availability_map = {}
    for idx, id in enumerate(ids):
        if idx < len(per_item_availability):
            availability_map[id] = per_item_availability[idx].get("available", False)
        else:
            availability_map[id] = False

    # Update each item in cart_items with service_eligible based on availability_map
    for item in cart_items:
        id = item.get("id")
        if id:
            item["service_eligible"] = availability_map.get(id, False)
        else:
            item["service_eligible"] = False

    return cart_items

def cart_analyzer_tool(tool_context: ToolContext) -> dict:
    """
    Analyzes the cart to determine if it contains service-eligible items.
    Adds a 'service_eligible' boolean to each item in the cart.
    
    Args:
        cart (list): A list of items in the cart. Each item should be a dictionary with at least a 'name' key.
        
    Returns:
        dict: A summary of the analysis, including whether service-eligible items are present and the updated cart.
    """
    # Define keywords that typically indicate service eligibility
    service_keywords = ["wardrobe", "bed", "cabinet", "shelf", "mount", "table", "sofa", "desk", "furniture", "frame"]

    updated_cart = []
    service_eligible_items = []

     # Get current cart 
    current_cart_details = tool_context.state.get("cart_details", [])

    updated_cart = batch_check_service_eligibility(current_cart_details)

    for item in current_cart_details:
        id = item.get("id")
        if id:
            item["service_eligible"] = check_service_eligibility(id)
        else:
            item["service_eligible"] = False  # or handle error/log
            
    for item in current_cart_details:
        item_name = item.get("name", "").lower()
        is_eligible = any(keyword in item_name for keyword in service_keywords)
        item["service_eligible"] = is_eligible

        updated_cart.append(item)

        if is_eligible:
            service_eligible_items.append(item)
    
    tool_context.state["cart_details"] = updated_cart

    return {
        "has_service_eligible_items": len(service_eligible_items) > 0,
        "service_eligible_items": service_eligible_items,
        "cart_details": updated_cart
    }
    
    return result

cart_analyzer_agent= Agent(
    name="cart_analyzer_agent",
    model="gemini-2.0-flash",
    description="This agent analyzes the cart to determine if it contains service-eligible items.",
    instruction="""
    You are an intelligent assistant at IKEA checkout. Your task is to analyze the current cart and determine if it contains service-eligible items.
    Your tasks include:
    1. Reads product IDs or names in the user’s cart and analyzes them to determine if they are service-eligible items using the cart_analyzer_tool only
    2. Providing a summary of which items are service-eligible
    3. Communicating with other agents as needed to facilitate the execution of tasks.
    4. Ensuring that it only uses the cart_analyzer_tool to analyze the cart.
    5. Maintaining a record of the analysis for future reference.
        """,
    tools=[cart_analyzer_tool],
    sub_agents=[],
)
