#!/usr/bin/env python3
import asyncio
import json
import logging
import os
import sys
import requests

# MCP Server Imports
from mcp import types as mcp_types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# Your schema imports
from schemas import (
    ListProductsInput,
    ListProductsOutput,
    GetProductDetailsInput,
    GetProductDetailsOutput,
    FetchServicePricesInput,
    FetchServicePricesOutput,
    EligibleItem,
    Configuration,
    fetch_service_prices_input_schema,
    cart_details_input_schema,
    CartItemsOutput,
)

from tools.service_macher import fetch_service_prices
from tools.list_products import list_products
from tools.get_product_details import get_product_details
from tools.get_cart_analysis import analyze_cart

from openai_generator import generate_openapi_spec

# --- Logging Setup ---
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "mcp_server_activity.log")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE_PATH, mode="w")],
)


# --- Tool Definitions ---
mcp_tools = [
    mcp_types.Tool(
        name="list-products",
        description="List available products",
        inputSchema=ListProductsInput.model_json_schema(),
        outputSchema=ListProductsOutput.model_json_schema(),
    ),
    mcp_types.Tool(
        name="get-product-details",
        description="Get details for a specific product",
        inputSchema=GetProductDetailsInput.model_json_schema(),
        outputSchema=GetProductDetailsOutput.model_json_schema(),
    ),
    mcp_types.Tool(
        name="fetch-service-prices",
        description="Fetch service prices for eligible items",
        inputSchema=fetch_service_prices_input_schema,
        outputSchema=FetchServicePricesOutput.model_json_schema(),
    ),
    mcp_types.Tool(
        name="analyze-cart",
        description="Analyze the cart to determine service eligibility",
        inputSchema=cart_details_input_schema,
        outputSchema=CartItemsOutput.model_json_schema(),
    )
]

# --- MCP Server Initialization ---
app = Server("minimal-mcp-server")

@app.list_tools()
async def list_mcp_tools() -> list[mcp_types.Tool]:
    return mcp_tools

@app.call_tool()
async def call_mcp_tool(name: str, arguments: dict) -> list[mcp_types.TextContent]:
    logging.info(f"Received tool call: {name} with arguments {arguments}")
    if name == "list-products":
        validated_args = ListProductsInput(**arguments)  # will raise validation error if wrong
        products = list_products()
        return [mcp_types.TextContent(type="text", text=json.dumps(products))]
    elif name == "get-product-details":
        validated_args = GetProductDetailsInput(**arguments)
        product_name = validated_args.productId
        details = get_product_details(product_name)
        return [mcp_types.TextContent(type="text", text=json.dumps(details))]
    elif name == "fetch-service-prices":
        
        pricing_info = fetch_service_prices(
            eligible_items=arguments.get("eligibleItems", []),
            retail_id=arguments.get("retailId", ""),
            zip_code=arguments.get("zipCode", "")
        )
        logging.info(f"Fetched service prices: {pricing_info}")
        return [mcp_types.TextContent(type="text", text=json.dumps(pricing_info))]
    elif name == "analyze-cart":
       
        analyzed_cart_items = analyze_cart(arguments.get("cart_items", []))
        logging.info(f"Analyzed cart: {analyzed_cart_items}")
        return [mcp_types.TextContent(type="text", text=json.dumps(analyzed_cart_items))]
    else:
        return [mcp_types.TextContent(type="text", text=json.dumps({"error": "Unknown tool"}))]



# --- Run MCP server over stdio ---
async def run_server():
    import mcp.server.stdio
    async with mcp.server.stdio.stdio_server() as (reader, writer):
        logging.info("Starting MCP stdio server")
        await app.run(
            reader,
            writer,
            InitializationOptions(
                server_name=app.name,
                server_version="0.1.0",
                capabilities=app.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        logging.info("MCP stdio server stopped")

if __name__ == "__main__":
    logging.info("Launching MCP server...")
    spec = generate_openapi_spec(mcp_tools)
    with open("openapi.json", "w") as f:
        json.dump(spec, f, indent=2)
    print("✅ OpenAPI spec written to openapi.json")
    asyncio.run(run_server())