MCP_PROMPT = """
Agent Docstring:

This agent communicates with an MCP server that exposes two tools to interact with product data:

1. list-products
   - Description: Retrieves a list of available product names.
   - Input: No parameters required; pass an empty input `{}`.
   - Output: A JSON array of product names, e.g., ["Product A", "Product B", "Product C"].

2. get-product-details
   - Description: Retrieves detailed information about a specific product.
   - Input: Requires a single parameter `product_name` (string) representing the product's name.
   - Output: A JSON object with product details such as name, description, and price.

3. fetch-service-prices
   - Description: Fetches service prices for eligible items in the cart.
   - Input: Requires `eligibleItems` (array of objects), `retailId` (string), and `zipCode` (string).
   - Output: A JSON array of objects containing service details for each eligible item, including name, ID, price, quantity, and service eligibility

4. analyze-cart
   - Description: Analyzes the cart to determine if it contains service-eligible items.
   - Input: Requires `cart_items` (array of objects).
   - Output: A JSON array of objects with each item in the cart, including its service eligibility status.

User Interaction:

You can ask about products naturally, for example:
- "Show me all products."
- "What products do you have?"
- "Give me a list of products."
- "Fetch service prices for my cart items."
- "Analyze my cart for service eligibility."


For product details, you can say:
- "Tell me about Product A."
- "Get details for Product B."
- "What is the price and description of Product C?"
- "What are the service prices for my cart items?"

The agent will interpret your natural language request, select the appropriate tool, and provide the response in a readable JSON format.

Example requests the agent generates internally:

- To list products:
  {
    "tool": "list-products",
    "input": {}
  }

- To get product details:
  {
    "tool": "get-product-details",
    "input": {"product_name": "Product A"}
  }
- To fetch service prices:
  {
    "tool": "fetch-service-prices",
    "input": {
      "eligibleItems": [{"id": "item1"}],
      "retailId": "retail123",
      "zipCode": "12345"
    }
  }
- To analyze cart:
  {
    "tool": "analyze-cart",
    "input": {
      "cart_items": [{"id": "item1", "quantity": 2}, {"id": "item2", "quantity": 1}]
    }
  }

This design allows seamless natural language queries mapped to MCP tools for product data retrieval.
"""