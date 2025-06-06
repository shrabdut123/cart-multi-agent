from google.adk.agents import Agent
import google.adk.tools.tool_context as ToolContext

def service_matcher_tool(tool_context: ToolContext) -> dict:
    """
    Matches service-eligible IKEA items to the corresponding available services
    (e.g., Assembly, Wall Mounting) based on SKU lookups from the internal eligibility database.

    Args:
        tool_context (ToolContext): The context containing the current state and cart details.
        
    Returns:
        dict: A mapping of item SKUs to the list of eligible services.
    """
    # Mocked IKEA internal SKU-to-service mapping (replace with API/DB call in production)
    ikea_service_eligibility_db = {
        "FURN-001": ["Assembly"],  # Kallax Shelf Unit
        "KIT-005": ["Wall Mounting"],  # Kitchen Cabinet Base
        "FURN-003": ["Assembly"],  # Platsa Wardrobe Frame
        "FURN-002": ["Installation"],  # Office Chair Markus - no service needed
        "ACC-004": ["Removal"],  # LED Lightbulb - no service
        "FURN-006": ["Wall Mounting"],  # LACK Wall Shelf
        "FURN-007": ["Assembly"],  # MALM Bed Frame
        "FURN-008": ["Assembly"],  # BRIMNES TV Unit
        "SVC-100": []  # Assembly Service Voucher - service item itself
    }

    result = {}

    # Get current cart 
    current_cart_details = tool_context.state.get("cart_details", [])
    print("Current cart details:", current_cart_details)
    if not current_cart_details:
        return {"error": "No items found in the cart."}
    
    updated_cart = []
    
    # Filter eligible items from the cart
    eligible_items = [
        item for item in current_cart_details if item.get("service_eligible", False)
        and "sku" in item and "name" in item
    ]
    if not eligible_items:
        return {"error": "No service-eligible items found in the cart."}

    for item in eligible_items:
        sku = item.get("sku")
        name = item.get("name", "Unknown Product")
        services = ikea_service_eligibility_db.get(sku, [])
        print(f"Processing item: {name} (SKU: {sku}) - Eligible Services: {services}, {bool(services)}")
        updated_cart.append({
            "name": name,
            "sku": sku,
            "service_eligible": bool(services),
            "services": services
        })
        result[sku] = {
            "name": name,
            "eligible_services": services
        }
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

        You will use the `service_matcher_tool` to match each item's SKU with IKEA's internal service eligibility database.
        You will then present the user with a summary of the eligible services for each item.
        You will not guess or fabricate services, and you will only use the `service_matcher_tool` to determine eligible services.
        

        Important:
        - Do not guess or fabricate services.
        - Only use the `service_matcher_tool` to determine matching services.
        """,
    sub_agents=[],
    tools=[service_matcher_tool],
)