def get_product_details(product_name: str) -> dict:
    return {
        "name": product_name,
        "description": f"Details of {product_name}",
        "price": 19.99,
    }