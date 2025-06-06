from google.adk.agents import Agent
import google.adk.tools.tool_context as ToolContext
import requests

def fetch_service_prices(eligible_items, retail_id, zip_code):
    url = 'https://service-offers-stage-o2jblwt7ia-ew.a.run.app/graphql'
    headers = {'content-type': 'application/json'}

    # Prepare item list for the GraphQL call
    graphql_items = [
        {
            "itemNo": item.get("id"),
            "itemType": item.get("itemType"),
            "quantity": item.get("quantity", 1)
        }
        for item in eligible_items if item.get("id")
    ]
    print("Inside graphql_items:::", graphql_items)

    query = """
    query ServicePrices($retailId: String!, $zipCode: String, $items: [InputItem]) {
      servicePrices(retailId: $retailId, zipCode: $zipCode) {
        SGR50000960(items: $items) {
          items {
            itemNo
            unitPrice {
              inclTax
            }
            subTotalPrice {
              inclTax
            }
          }
          configuration {
            basePrice
            provider
            serviceInfo {
              id
              method
              type
            }
          }
        }
      }
    }
    """

    variables = {
        "retailId": retail_id,
        "zipCode": zip_code,
        "items": graphql_items
    }

    response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
    response.raise_for_status()
    data = response.json()
    print("Response from service prices API:", data)

    # Parse servicePrices -> SGR50000960
    pricing_info = data.get("data", {}).get("servicePrices", {}).get("SGR50000960", {})
    print("Parsed pricing info:", pricing_info)
    pricing_items = pricing_info.get("items", [])
    print("Pricing items:", pricing_items)
    configuration = pricing_info.get("configuration", {})
    print("Configuration:", configuration)

    # Build maps for quick lookup
    price_lookup = {
        item["itemNo"]: {
            "unit_price": item["unitPrice"]["inclTax"],
            "sub_total": item["subTotalPrice"]["inclTax"]
        } for item in pricing_items
    }
    print("Price lookup map:", price_lookup)
    updated_cart = []
    for item in eligible_items:
        # Defensive: Ensure item is a dictionary
        if not isinstance(item, dict):
            print(f"⚠️ Skipping non-dict item: {item}")
            continue

        # Try to get 'id'
        item_id = item.get("id")
        if not item_id or not isinstance(item_id, str):
            print(f"⚠️ Skipping item with invalid or missing ID: {item}")
            continue

        name = item.get("name", "Unknown Product")
        quantity = item.get("quantity", 1)

        price = item.get("price", 0.0)  # Ensure price is set, default to 0.0

        print(f"🛠️ Processing item: {name} (ID: {item_id}, Qty: {quantity})")

        # Defensive: Look up pricing safely
        pricing = price_lookup.get(str(item_id), {})
        if not isinstance(pricing, dict):
            print(f"⚠️ Invalid pricing format for item {item_id}: {pricing}")
            pricing = {}

        unit_price = pricing.get("unit_price", 0)
        sub_total = pricing.get("sub_total", 0)

        print(f"💰 Pricing - Unit: {unit_price}, Subtotal: {sub_total}")

        # Defensive: Ensure configuration exists and is a dict
        if not isinstance(configuration, dict):
            print("⚠️ Invalid configuration object.")
            configuration = {}

        service_info = configuration.get("serviceInfo")

        print(f"📦 serviceInfo: {service_info}")
        services = []
        services.append({
                "id": service_info.get("id"),
                "method": service_info.get("method"),
                "type": service_info.get("type"),
                "provider": configuration.get("provider"),
                "base_price": configuration.get("basePrice"),
                "unit_price": unit_price,
                "sub_total": sub_total
            })

        print(f"✅ Final services for {item_id}: {services}")

        # Append to updated cart
        print ("Updated cart item:", {
            "name": name,
            "id": item_id,
            "price": price,
            "quantity": quantity,
            "service_eligible": bool(services),
            "services": services
        })

        updated_cart.append({
            "name": name,
            "id": item_id,
            "price": price,
            "quantity": quantity,
            "service_eligible": bool(services),
            "services": services
        })
    print("Final updated cart:", updated_cart)
    return updated_cart


def service_matcher_tool(tool_context: ToolContext, retail_id: str, zip_code: str) -> dict:
    """
    Matches service-eligible IKEA items to the corresponding available services

    Args:
        tool_context (ToolContext): The context containing the current state and cart details.
        retail_id (str): The retail ID for the IKEA store.
        zip_code (str): The zip code for the user's location to check service availability.
        
    Returns:
        The updated cart with all the items that are eligible for services along with quantity and total prices and their corresponding service details.
    """

    # Get current cart 
    current_cart_details = tool_context.state.get("cart_details", [])
    if not current_cart_details:
        return {"error": "No items found in the cart."}
    
    updated_cart = []
    
    # Filter eligible items from the cart
    eligible_items = [
        item for item in current_cart_details if item.get("service_eligible", False)
        and "id" in item and "name" in item
    ]
    if not eligible_items:
        return {"error": "No service-eligible items found in the cart."}

    updated_cart = fetch_service_prices(eligible_items, retail_id, zip_code)
    tool_context.state["cart_details"] = updated_cart

    return updated_cart

service_matcher_agent = Agent(
    name="service_matcher_agent",
    model="gemini-2.0-flash",
    description="This agent matches services to the cart based on the analysis provided by the cart_analyzer_agent.",
    instruction="""
        You are a service matcher agent.

        Your primary task is to help users determine which IKEA services are available 
        (e.g., Assembly, Wall Mounting) for the items in their cart that are eligible for services using the `service_matcher_tool`.

        You will then present the user with a summary of the eligible services for each item that includes items , eligible serbices , provider , unit prices, base price and total prices.
        You will not guess or fabricate services, and you will only use the `service_matcher_tool` to determine eligible services.
        

        Important:
        - Do not guess or fabricate services.
        - Only use the `service_matcher_tool` to determine matching services.
        """,
    sub_agents=[],
    tools=[service_matcher_tool],
)