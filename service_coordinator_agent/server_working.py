import sys
import os
import logging

#!/usr/bin/env python3
import asyncio
import json

# MCP Server Imports
from mcp import types as mcp_types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# Add the generated client folder to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "generated_client"))

# Add generated weather client
sys.path.insert(0, os.path.join(BASE_DIR, "generated_weather_client"))

#Add the generated client for sales item
sys.path.insert(0, os.path.join(BASE_DIR, "generated_salesitem_client"))

# Add the generated client for order capture
sys.path.insert(0, os.path.join(BASE_DIR, "generated_order_capture_client"))

from openapi_client.api_client import ApiClient  # adjust imports to match your generated client
from openapi_client.api.default_api import DefaultApi
from openapi_client.configuration import Configuration
from openapi_client.models import FetchServicePricesRequest
from typing import Any, Dict
from pathlib import Path

# Import from weather client
from weather_client.api_client import ApiClient as WeatherApiClient
from weather_client.api.default_api import DefaultApi as WeatherDefaultApi
from weather_client.configuration import Configuration as WeatherConfiguration

# Import from sales item client
from salesitem_client.api_client import ApiClient as SalesItemApiClient
from salesitem_client.api.sales_price_api import SalesPriceApi

from salesitem_client.configuration import Configuration as SalesItemConfiguration

# Import the available classifications

from salesitem_client.api.availability_classification_api import AvailabilityClassificationApi

# Import from order capture client
from order_capture_client.api_client import ApiClient as CheckoutApiClient
from order_capture_client.api.checkout_api import CheckoutApi
from order_capture_client.api.checkout_service_area_api import CheckoutServiceAreaApi
from order_capture_client.api.checkout_deliver_services_delivery_time_windows_service_time_windows_api import CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi
from order_capture_client.configuration import Configuration as OrderCaptureConfiguration
from order_capture_client.models import DSResponseDto


# --- Logging Setup ---
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "mcp_server_activity.log")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE_PATH, mode="w")],
)

# 1️⃣ Configure the API client
config = Configuration(
    host="https://service-offers-stage-o2jblwt7ia-ew.a.run.app/graphql"  # Replace with your endpoint
)
client = ApiClient(configuration=config)
client_api = DefaultApi(client)

# 2️⃣ Configure the weather API client
weather_config = WeatherConfiguration()
weather_client = WeatherApiClient(configuration=weather_config)
weatherClient_api = WeatherDefaultApi(weather_client)

# 3️⃣ Configure the sales item API client
sales_item_config = SalesItemConfiguration("https://api.salesitem.ingka.com")
# Set the API key using the security scheme name from the spec
sales_item_config.api_key["clientIDHeader"] = "54e397b3-cd11-46d3-bdb8-9a6721b4fce4"
sales_item_client = SalesItemApiClient(configuration=sales_item_config)
# Create the sales item API instance
salesClient_api = SalesPriceApi(sales_item_client)

# 4️⃣ Configure the order capture API client
order_capture_config = OrderCaptureConfiguration("https://ordercapture.ingka.com/ordercaptureapi")
# Set the API key using the security scheme name from the spec
order_capture_config.api_key["Client-Id"] = "af2525c3-1779-49be-8d7d-adf32cac1934"
order_capture_config.access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImVxSFFLR3duR3hfV3dJZkx0RGpaeDA5MTUzS2xSam5fVE1nVUlMYlJ5RncifQ.eyJpc3MiOiJodHRwczovL2FwaS5pbmdrYS5pa2VhLmNvbS9ndWVzdCIsInN1YiI6IjVkMzQ2MDBlLWNhNzAtNDQyMi04YTRjLTBiYzcwZGY1NDU2YiIsInJldGFpbFVuaXQiOiJzZSIsImlhdCI6MTc1NTYzODA5OSwiZXhwIjoxNzU4MjMwMDk5fQ.QW73661YeEifypqIzks7gLnssSzq0_ixvOHb7T3l3tCtrjLjWWyLWh8-h-uEw0pY6EhAHKttLs4gER6p5Ue0AR0d6wMQn3EsSG_7Sv8b5WufrtmnxGlF7g-T7ftHVQq09I10fN5V3xLcE5MzrrPTOWd-iTclYr-g6l0GHGaxU1E"
order_capture_client = CheckoutApiClient(configuration=order_capture_config)
# Create the order capture API instance
order_capture_api = CheckoutApi(order_capture_client)
order_capture_service_area_api = CheckoutServiceAreaApi(order_capture_client)
order_capture_delivery_services_time_windows_api = CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(order_capture_client)


# --- MCP Server Initialization ---
app = Server("minimal-mcp-server")

dummy_request = FetchServicePricesRequest(query="", variables={})
input_schema_json = dummy_request.to_json()  # returns JSON string
input_schema_dict = json.loads(input_schema_json)  # convert back to dict


generic_input_schema = {
    "type": "object",
    "description": "Wrapper for GraphQL variables. Put all user input inside 'variables'.",
    "properties": {
        "variables": {
            "type": "object",
            "description": "GraphQL variables object (any key-value pairs).",
            "additionalProperties": True
        }
    },
    "required": ["variables"],
}

mcp_tools = [
    mcp_types.Tool(
        name="fetch-service-prices",
        description="Fetch service prices from GraphQL endpoint",
        inputSchema=generic_input_schema,
    ),
    mcp_types.Tool(
        name="get-weather",
        description="Fetch weather from REST endpint",
        inputSchema={
            "type": "object",
            "description": "Get current weather based on latitude and longitude.",
            "properties": {
                "latitude": {
                    "type": "number",
                    "description": "Latitude of the location."
                },
                "longitude": {
                    "type": "number",
                    "description": "Longitude of the location."
                }
            },
            "required": ["latitude", "longitude"]
        },
    ),
    mcp_types.Tool(
        name="fetch-sales-item-prices",
        description="Fetch sales item prices from REST endpoint",
        inputSchema={
            "type": "object",
            "title": "GetItemSalesPricesInput",
            "description": "Input schema for fetching sales price information of an IKEA sales item",
            "properties": {
                "classUnitType": {
                "type": "string",
                "description": "`classUnitType` can be either Retail Unit/Market (`ru`) or Store (`sto`).",
                "enum": ["ru", "sto"]
                },
                "classUnitCode": {
                "type": "string",
                "description": "Unique identifier of a Class Unit, combined with classUnitType. Pattern like `^([A-Z]|[0-9]){2,5}$`.",
                "minLength": 2,
                "maxLength": 5
                },
                "itemNos": {
                "type": "string",
                "description": "Item number of the IKEA item/product. Supports ART, SGR, SPR types. Between 1 and 50 per request.",
                "minLength": 8,
                "maxLength": 799
                },
                "languageCode": {
                "type": "string",
                "description": "Two-letter ISO language code filter (e.g., 'en', 'sv'). If not defined, returns all languages.",
                "pattern": "^[a-z][a-z]$",
                "minLength": 2,
                "maxLength": 2
                }
            },
            "required": ["classUnitType", "classUnitCode", "itemNos"]
            }
    ),
    mcp_types.Tool(
        name="fetch-available-classifications",
        description="Fetch available classifications from sales item API",
       inputSchema = {
            "type": "object",
            "title": "GetAvailableClassificationsInput",
            "description": "Input schema for fetching available classifications from the AvailabilityClassifications API.",
            "properties": {
                "classUnitType": {
                    "type": "string",
                    "description": "Must be `ru`. It is used together with `classUnitCode` to give context when invoking AvailabilityClassifications API.",
                    "enum": ["ru"]
                },
                "classUnitCode": {
                    "type": "string",
                    "description": "Unique identifier of a Class Unit. Pattern: ^([A-Z]|[0-9]){2,5}$",
                    "minLength": 2,
                    "maxLength": 5,
                    "pattern": "^([A-Z]|[0-9]){2,5}$"
                },
                "channel": {
                    "type": "string",
                    "description": "Optional filter to find a rule for a specific channel. If not passed, all channels are returned. ALL indicates channel independent.",
                    "enum": [
                        "CUSTOMER_SUPPORT_CENTRE",
                        "STORE",
                        "ONLINE",
                        "ALL"
                    ]
                },
                "type": {
                    "type": "string",
                    "description": "Optional filter to find a specific classification type. If not passed, all types are returned. Note: CASH_AND_CARRY and HOME_DELIVERY are deprecated and moved to CIA API.",
                    "enum": [
                        "CASH_AND_CARRY",
                        "HOME_DELIVERY",
                        "COLLECT",
                        "CUSTOMER_PURCHASE",
                        "CUSTOMER_COMMUNICATION",
                        "PARCEL_ELIGIBLE",
                        "INTENDED_FOR_HOME_DELIVERY"
                    ]
                },
                "itemNos": {
                    "type": "string",
                    "description": "One or many item numbers (max 50). If more than one, separate with commas.",
                    "minLength": 0,
                    "maxLength": 799
                },
                "value": {
                    "type": "boolean",
                    "description": "Optional filter to find a specific classification value, true or false. If not passed, all values are returned."
                },
                "itemType": {
                    "type": "string",
                    "description": "Optional filter to find a specific item type. If not passed, all types are returned.",
                    "enum": [
                        "ART",
                        "SPR"
                    ]
                }
            },
            "required": ["classUnitType", "classUnitCode","itemNos"]
        }
    ),
    mcp_types.Tool(
        name="initiate-checkout",
        description="Initiate a checkout process in the order capture system",
        inputSchema = {
            "type": "object",
            "properties": {
                "retailUnit": {
                    "type": "string",
                    "description": "Retail unit identifier (path parameter)",
                    "example": "us123"
                },
                "checkoutRequest": {
                    "type": "object",
                    "required": ["channel", "items", "languageCode", "shoppingType"],
                    "properties": {
                        "shoppingType": {
                            "type": "string",
                            "enum": ["ONLINE", "NO_STOCK_STORE_ORDER", "NO_STOCK_WEB_ORDER"],
                            "example": "ONLINE"
                        },
                        "channel": {
                            "type": "string",
                            "enum": ["WEBAPP", "MOBILE_APP"],
                            "example": "WEBAPP"
                        },
                        "shoppingAppPlatform": {
                            "type": "string",
                            "enum": ["IKEAAPP_IOS", "IKEAAPP_ANDROID", "WEB_BROWSER", "B2B_ONLINE"],
                            "example": "WEB_BROWSER"
                        },
                        "familyCardNo": {"type": "string", "example": "1233645878937646"},
                        "applyEmployeeDiscount": {"type": "boolean", "example": True},
                        "profileType": {"type": "string", "enum": ["REGULAR", "BUSINESS"], "example": "REGULAR"},
                        "deliveryArea": {"type": "object"},
                        "serviceArea": {"type": "object"},
                        "cartCheckSum": {"type": "string", "example": "fdsgoiu98739q8u"},
                        "languageCode": {"type": "string", "example": "en"},
                        "consumerInfo": {"type": "object"},
                        "items": {
                            "type": "array",
                            "items": {"type": "object"}
                        },
                        "serviceItems": {
                            "type": "array",
                            "items": {"type": "object"}
                        },
                        "removalServiceItems": {
                            "type": "array",
                            "items": {"type": "object"}
                        },
                        "coupon": {"type": "object"},
                        "shippingContacts": {
                            "type": "array",
                            "items": {"type": "object"}
                        },
                        "vpcCodes": {
                            "type": "array",
                            "items": {"type": "string", "example": "9JMV3V"}
                        },
                        "consents": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["TIPPING_HAZARD", "TASKRABBIT", "NEED_HELP"], "example": "TIPPING_HAZARD"}
                        }
                    }
                }
            },
            "required": ["retailUnit", "checkoutRequest"]
        }
    ),
    mcp_types.Tool(
        name="set-service-area",
        description="Set service area for a checkout in the order capture system",
        inputSchema={
            "type": "object",
            "properties": {
                "checkoutId": {
                    "type": "string",
                    "description": "Checkout ID (path parameter)",
                    "example": "123456"
                },
                "retailUnit": {
                    "type": "string",
                    "description": "Retail unit identifier (path parameter)",
                    "example": "se"
                },
                "serviceAreaRequest": {
                        "type": "object",
                        "required": ["zipCode"],
                        "properties": {
                            "zipCode": {
                                "type": "string",
                                "description": "Postal code for the service area",
                                "example": "25185"
                            },
                            "stateCode": {
                                "type": "string",
                                "description": "Mandatory for US",
                                "example": "PR"
                            },
                            "city": {
                                "type": "string",
                                "description": "City for the service area",
                                "example": "Helsingborg"
                            },
                            "deliveryCountryCode": {
                                "type": "string",
                                "description": "Used if delivery is to another country (special cases, e.g., Luxembourg)",
                                "example": "LU"
                            }
                        },
                        "description": "Details of the delivery/service area"
                    }
                },
                "required": ["checkoutId", "retailUnit", "serviceAreaRequest"]
        },
    ),
    mcp_types.Tool(
        name="fetch-home-delivery-services",
        description="Fetch home delivery services for a given retail unit and zip code",
        inputSchema= {
            "type": "object",
            "properties": {
                "serviceAreaId": {
                    "type": "string",
                    "description": "Service area identifier (path parameter)",
                    "example": "sa_12345"
                },
                "checkoutId": {
                    "type": "string",
                    "description": "Checkout ID (path parameter)",
                    "example": "co_98765"
                },
                "retailUnit": {
                    "type": "string",
                    "description": "Retail unit identifier (path parameter)",
                    "example": "se"
                }
            },
            "required": ["serviceAreaId", "checkoutId", "retailUnit"]
        }
            
    )

]

@app.list_tools()
async def list_mcp_tools() -> list[mcp_types.Tool]:
    return mcp_tools

@app.call_tool()
async def call_mcp_tool(name: str, arguments: dict) -> list[mcp_types.TextContent]:
    if name == "get-weather":
        logging.info(f"Received tool call: {name} with arguments {arguments}")
        latitude = arguments.get("latitude")
        longitude = arguments.get("longitude")
        if latitude is None or longitude is None:
            logging.error("Latitude and longitude are required for weather API call.")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": "Latitude and longitude are required"}))]
        try:
            # Call the weather API
            response = weatherClient_api.forecast_get(latitude=latitude, longitude=longitude)
            logging.info(f"Weather API response: {response}")
            response_dict = response.to_dict()
            response_json = json.dumps(response_dict, indent=2, default=str)  # make datetime serializable

            return [mcp_types.TextContent(type="text", text=response_json)]
        except Exception as e:
            logging.error(f"Error fetching weather data: {e}")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": str(e)}))]
    
    if name == "fetch-sales-item-prices":
        logging.info(f"Received tool call: {name} with arguments {arguments}")
        class_unit_type = arguments.get("classUnitType")
        class_unit_code = arguments.get("classUnitCode")
        item_nos = arguments.get("itemNos")
        language_code = arguments.get("languageCode")

        if not all([class_unit_type, class_unit_code, item_nos]):
            logging.error("classUnitType, classUnitCode, and itemNos are required for sales item prices.")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": "Missing required parameters"}))]

        try:
            # Call the sales item API
            response = salesClient_api.get_item_sales_prices(
                class_unit_type=class_unit_type,
                class_unit_code=class_unit_code,
                item_nos=item_nos,
                language_code=language_code
            )
            logging.info(f"Sales Item API response: {response}")
            response_dict = response.to_dict()
            response_json = json.dumps(response_dict, indent=2, default=str)  # make datetime serializable

            return [mcp_types.TextContent(type="text", text=response_json)]
        except Exception as e:
            logging.error(f"Error fetching sales item prices: {e}")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": str(e)}))]

    if name == "fetch-available-classifications":
        logging.info(f"Received tool call: {name} with arguments {arguments}")
        class_unit_type = arguments.get("classUnitType")
        class_unit_code = arguments.get("classUnitCode")
        item_nos = arguments.get("itemNos", None)

        if not class_unit_type or not class_unit_code:
            logging.error("classUnitType and classUnitCode are required for available classifications.")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": "Missing required parameters"}))]

        try:
            # Call the available classifications API
            available_classifications_api = AvailabilityClassificationApi(sales_item_client)
            response = available_classifications_api.get_item_availability_classifications(
                class_unit_type=class_unit_type,
                class_unit_code=class_unit_code,
                item_nos=item_nos,
            )
            logging.info(f"Available Classifications API response: {response}")
            response_dict = response.to_dict()
            response_json = json.dumps(response_dict, indent=2, default=str)  # make datetime serializable

            return [mcp_types.TextContent(type="text", text=response_json)]
        except Exception as e:
            logging.error(f"Error fetching available classifications: {e}")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": str(e)}))]

    if name == "fetch-service-prices":
        logging.info(f"Received tool call: {name} with arguments {arguments}")

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
        vars_in = arguments.get("variables", {})

        # Transform ADK arguments into GraphQL variables
        variables = {
            "retailId": vars_in.get("retailId"),
            "zipCode": vars_in.get("zipCode"),
            "items": [
                {
                    "itemNo": item.get("id"),          # map `id` -> `itemNo`
                    "itemType": item.get("itemType"),
                    "quantity": item.get("quantity")
                }
                for item in vars_in.get("eligibleItems", [])
            ]
        }
        

        logging.info(f"Received query for {name}: {query}")
        logging.info(f"Received variables for {name}: {variables}")

        # Call your GraphQL wrapper function
        request = FetchServicePricesRequest(query=query, variables=variables)
        result = client_api.fetch_service_prices(request)
        logging.info(f"Result from tool {result}")

        # Return in MCP-compatible format
        return [mcp_types.TextContent(type="text", text=json.dumps(result))]

    if name == "initiate-checkout":
        logging.info(f"Received tool call: {name} with arguments {arguments}")
        retail_unit = arguments.get("retailUnit")
        checkout_request = arguments.get("checkoutRequest")

        if not retail_unit or not checkout_request:
            logging.error("retailUnit and checkoutRequest are required for initiating checkout.")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": "Missing required parameters"}))]

        try:
            # Call the order capture API
            response = order_capture_api.create_checkout(
                retail_unit=retail_unit,
                checkout_request=checkout_request
            )
            logging.info(f"Order Capture API response: {response}")
            response_dict = response.to_dict()
            response_json = json.dumps(response_dict, indent=2, default=str)  # make datetime serializable
            logging.info(f"Checkout initiated successfully: {response_json}")
            return [mcp_types.TextContent(type="text", text=response_json)]
        except Exception as e:
            logging.error(f"Error initiating checkout: {e}")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": str(e)}))]

    if name == "set-service-area":
        logging.info(f"Received tool call: {name} with arguments {arguments}")
        checkout_id = arguments.get("checkoutId")
        retail_unit = arguments.get("retailUnit")
        service_area_request = arguments.get("serviceAreaRequest")

        if not checkout_id or not retail_unit or not service_area_request:
            logging.error("checkoutId, retailUnit, and serviceAreaRequest are required for setting service area.")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": "Missing required parameters"}))]

        try:
            # Call the order capture API to set service area
            response = order_capture_service_area_api.create_service_area(
                checkout_id=checkout_id,
                retail_unit=retail_unit,
                service_area_request=service_area_request
            )
            logging.info(f"Order Capture API response: {response}")
            response_dict = response.to_dict()
            response_json = json.dumps(response_dict, indent=2, default=str)  # make datetime serializable

            return [mcp_types.TextContent(type="text", text=response_json)]
        except Exception as e:
            logging.error(f"Error setting service area: {e}")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": str(e)}))]
    
    if name == "fetch-home-delivery-services":
        logging.info(f"Received tool call: {name} with arguments {arguments}")
        service_area_id = arguments.get("serviceAreaId")
        checkout_id = arguments.get("checkoutId")
        retail_unit = arguments.get("retailUnit")

        if not service_area_id or not checkout_id or not retail_unit:
            logging.error("serviceAreaId, checkoutId, and retailUnit are required for fetching home delivery services.")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": "Missing required parameters"}))]

        try:
            # Call the order capture API to fetch home delivery services
            response_obj: DSResponseDto = order_capture_delivery_services_time_windows_api.get_home_delivery_services(
                service_area_id=service_area_id,
                checkout_id=checkout_id,
                retail_unit=retail_unit
            )
           # Convert Pydantic model to dict (no validation errors)
            data = response_obj.model_dump(by_alias=True)  # safe dict representation
            logging.info(f"Order Capture DS API response: {data}")

            # Return as JSON string so MCP doesn’t choke on dict
            return [mcp_types.TextContent(type="text", text=json.dumps(data))]
        except Exception as e:
            logging.error(f"Error fetching home delivery services: {e}")
            return [mcp_types.TextContent(type="text", text=json.dumps({"error": str(e)}))]
    


    # Unknown tool fallback
    return [mcp_types.TextContent(type="text", text=json.dumps({"error": "unknown tool"}))]
    
    # --- Run MCP server over stdio ---
async def run_server():
    import mcp.server.stdio
    async with mcp.server.stdio.stdio_server() as (reader, writer):
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

if __name__ == "__main__":
    logging.info("Launching MCP server...")
    asyncio.run(run_server())