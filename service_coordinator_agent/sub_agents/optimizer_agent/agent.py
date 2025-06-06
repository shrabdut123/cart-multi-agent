from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from typing import Optional, List, Dict
from pydantic import BaseModel

        
def get_additional_items() -> List[Dict]:
    # Simulated item suggestions; ideally pulled from IKEA's product recommendation API
    return [
        {
            "name": "HEMNES Nightstand",
            "sku": "HEM123",
            "price": 69.0,
            "itemType": "furniture"
        },
        {
            "name": "LEN Sheet Set",
            "sku": "LEN456",
            "price": 35.0,
            "itemType": "textile"
        },
        {
            "name": "SKUBB Storage Boxes",
            "sku": "SKU789",
            "price": 12.0,
            "itemType": "small_item"
        }
    ]

def optimizer_tool(tool_context: ToolContext) -> dict:
    """
    This tool analyzes the current IKEA shopping cart to determine if the customer can reduce their effective delivery cost
    by adding more items. It is particularly useful when a flat-fee truck delivery is already triggered by large or bulky items.
    
    Args:
        tool_context (ToolContext): The context containing the current cart details and delivery details.
        
    Returns: The updated cart with optimization suggestions:
    """
    cart_details = tool_context.state.get("cart_details", [])
    message = tool_context.state.get("message", {})
    delivery_mode = tool_context.state.get("delivery_mode", {})
    delivery_price = tool_context.state.get("delivery_price", 0)
    total_cart_value = tool_context.state.get("total_cart_value", 0)

    if delivery_mode != "Truck Delivery":
        return {
            "cart_optimization": None,
            "recommendation_message": "This tool is only applicable for Truck Delivery mode.",
            "total_cart_value": 0,
            "item_count": 0,
            "shipping_cost_per_item": 0
        }
    
    item_count = len(cart_details)

    print("Total Value:", total_cart_value)
    print("Item Count:", item_count)

    if item_count == 0:
        return {
            "cart_optimization": None,
            "recommendation_message": "Your cart is empty. Please add items to optimize delivery costs.",
            "total_cart_value": 0,
            "item_count": 0,
            "shipping_cost_per_item": 0
        }
    
    shipping_cost_per_item = delivery_price / item_count if item_count > 0 else 0

    print("Shipping Cost Per Item:", shipping_cost_per_item)

    # Threshold logic for recommending optimization
    if shipping_cost_per_item < 20:
        return {
            "cart_optimization": None,
            "total_cart_value": total_cart_value,
            "item_count": item_count,
            "shipping_cost_per_item": round(shipping_cost_per_item, 2),
            "recommendation_message": "Your delivery cost per item is already low. No need to add more items."
        }
        
    elif total_cart_value < 100:
        return {
            "cart_optimization": None,
            "total_cart_value": total_cart_value,
            "item_count": item_count,
            "shipping_cost_per_item": round(shipping_cost_per_item, 2),
            "recommendation_message": "Your cart value is low. Consider adding more items to reduce delivery cost per item."
        }
            
    elif item_count >= 10:
        return {
            "cart_optimization": None,
            "total_cart_value": total_cart_value,
            "item_count": item_count,
            "shipping_cost_per_item": round(shipping_cost_per_item, 2),
            "recommendation_message": "You have a large number of items in your cart. Your delivery cost per item is already optimized."
        }
    elif shipping_cost_per_item > 20 or total_cart_value < 400:
        suggestions = get_additional_items()
        recommendation_message = (
            f"You're already paying a flat ${delivery_price} truck delivery fee. "
            "Adding a few more items can significantly reduce the delivery cost per item."
        )
        return {
            "cart_optimization": "Yes",
            "recommendation_message": recommendation_message,
            "total_cart_value": total_cart_value,
            "item_count": item_count,
            "shipping_cost_per_item": round(shipping_cost_per_item, 2),
            "suggested_items": suggestions
        }

optimizer_agent = Agent(
    name="optimizer_agent",
    model="gemini-2.0-flash",
    description="This sub-agent analyzes the current IKEA shopping cart to determine if the customer can reduce their effective delivery cost by adding more items. It is particularly useful when a flat-fee truck delivery is already triggered by large or bulky items.",
    instruction="""
    You are an intelligent assistant at IKEA checkout. Your task is to analyze the current cart and determine if the customer can reduce their effective delivery cost by adding more items.
    This is particularly useful when a flat-fee truck delivery is already triggered by large or bulky items.

    The agent optimizes the cart by calling the `optimizer_tool` to analyze the cart details and suggest additional items that can be added to lower the delivery cost per item.

    The tool will return a recommendation message, total cart value, item count, and shipping cost per item.
    
    """,
    sub_agents=[],
    tools=[optimizer_tool],
)