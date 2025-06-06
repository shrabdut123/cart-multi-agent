from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext


import requests

def batch_check_service_eligibility(cart_items):

    print("Checking service eligibility for cart items:", cart_items)
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
    print("Response status code:", response.status_code)
    response.raise_for_status()
    data = response.json()
    print("Response data:", data)

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
        item["price"] = item.get("price", 0.0)  # Ensure price is set, default to 0.0
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

    updated_cart = []

    # Load existing cart from state. If none exist, start wit a default cart
    current_cart_details = tool_context.state.get("cart_details", [
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
        }
    ])

    updated_cart = batch_check_service_eligibility(current_cart_details)

    tool_context.state["cart_details"] = updated_cart

    return {
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
