def upsell_recommendation_tool(cart_items) -> dict:
    """
    Recommends bundled service packages and upsell messages if multiple service-eligible items are found.

    Args:
        tool_context (ToolContext): The context containing the current state and cart details.

    Returns:
        dict: Recommendation summary with suggested bundle, item count, and upsell message.
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

    num_eligible = len(eligible_items)
    upsell_message = ""
    discount = 0

    # Placeholder logic for upsell message
    if num_eligible >= 10:
        discount = 1600
        upsell_message = (
            f"Wow! {num_eligible} items in your cart qualify for professional installation.\n"
            f"Bundle now and save ₹{discount} — our biggest discount yet!\n"
            "Let our experts handle the setup while you sit back and relax."
        )
    elif num_eligible == 9:
        discount = 1400
        upsell_message = (
            f"You’re eligible for a massive ₹{discount} discount on professional installation for 9 items!\n"
            "Perfect for full home furnishing setups."
        )
    elif num_eligible == 8:
        discount = 1200
        upsell_message = (
            "Your 8 eligible items can now be professionally installed.\n"
            f"Save ₹{discount} — your best move for convenience and savings!"
        )
    elif num_eligible == 7:
        discount = 1000
        upsell_message = (
            f"With 7 installable items, you qualify for ₹{discount} off installation services.\n"
            "Effortless setup, exceptional savings!"
        )
    elif num_eligible == 6:
        discount = 900
        upsell_message = (
            f"6 items ready for installation — unlock ₹{discount} in savings.\n"
            "Upgrade your experience with expert help!"
        )
    elif num_eligible == 5:
        discount = 800
        upsell_message = (
            f"You have 5 items eligible for installation services.\n"
            f"Bundle now to save ₹{discount} and skip the stress!"
        )
    # Continue with the previously listed 4 → 1 and default

    return {
        "num_service_eligible_items": num_eligible,
        "recommended_bundle": list(eligible_items),
        "upsell_message": upsell_message,
        "discount_value": discount
    }
