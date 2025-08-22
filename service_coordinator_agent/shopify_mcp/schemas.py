from typing import List, Optional, Literal
from pydantic import BaseModel, Field, conint, RootModel, confloat, conint


# -------------------------------
# list_products
# -------------------------------

class ListProductsInput(BaseModel):
    """No parameters required — returns all available products."""
    class Config:
        extra = "forbid"


class ListProductItem(BaseModel):
    """Represents a single product in the list."""
    id: str
    name: str
    category: Optional[str] = None

    class Config:
        extra = "forbid"


class ListProductsOutput(RootModel[List[ListProductItem]]):
    """A list of products."""
    root: List[ListProductItem]


# -------------------------------
# get_product_details
# -------------------------------

class GetProductDetailsInput(BaseModel):
    """Input to fetch details for a specific product."""
    productId: str

    class Config:
        extra = "forbid"


class GetProductDetailsOutput(BaseModel):
    """Detailed information for a product."""
    id: str
    name: str = Field(..., description="Name of the product")
    price: float
    available: bool

    class Config:
        extra = "forbid"


# -------------------------------
# fetch_service_prices
# -------------------------------

class EligibleItem(BaseModel):
    """Represents an eligible item for service pricing."""
    id: str = Field(..., description="Unique identifier for the item")
    itemType: str = Field(..., description="Type of the item")
    quantity:int = Field(..., ge=1, description="Quantity of the item")

    class Config:
        extra = "forbid"  # equivalent to additionalProperties=False


class FetchServicePricesInput(BaseModel):
    """Input schema for fetching service prices."""
    eligibleItems: List[EligibleItem] = Field(..., description="List of eligible items")
    retailId: str = Field(..., description="Retail store identifier")
    zipCode: str = Field(..., description="Zip/postal code for service pricing lookup")

    class Config:
        extra = "forbid"  # equivalent to additionalProperties=False


class PriceInfo(BaseModel):
    """Price information, including tax."""
    inclTax: float

    class Config:
        extra = "forbid"


class ServiceInfo(BaseModel):
    """Details about a service method."""
    id: str
    method: str
    type: str

    class Config:
        extra = "forbid"


class Configuration(BaseModel):
    """Configuration for service pricing."""
    basePrice: float
    provider: str
    serviceInfo: List[ServiceInfo]

    class Config:
        extra = "forbid"


class ItemPrice(BaseModel):
    """Pricing details for a specific item."""
    itemNo: str
    unitPrice: PriceInfo
    subTotalPrice: PriceInfo

    class Config:
        extra = "forbid"


class FetchServicePricesOutput(BaseModel):
    """Output containing service price details."""    
    items: List[ItemPrice] = Field(
        ...,
        description="List of items with their pricing details",
        example=[
            {
                "itemNo": "item1",
                "unitPrice": {"inclTax": 100.0},
                "subTotalPrice": {"inclTax": 200.0} 
            }
        ]
    )
    configuration: Configuration = Field(
        ...,
        description="Configuration details for the service pricing",
        example={
            "basePrice": 50.0,
            "provider": "Service Provider",
            "serviceInfo": [
                {"id": "service1", "method": "method1", "type": "type1"},
                {"id": "service2", "method": "method2", "type": "type2"}
            ]
        }
    )

    class Config:
        extra = "forbid"

fetch_service_prices_input_schema = {
    "type": "object",
    "description": "Input schema for fetching service prices",
    "properties": {
        "eligibleItems": {
            "type": "array",
            "description": "A list of eligible items to fetch service prices for. Must contain at least one item.",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "minLength": 1, "maxLength": 10},
                    "itemType": {"type": "string", "minLength": 2, "maxLength": 20, "enum": ["ART", "SPR"], "description": "Type of the item, e.g., ART for art items, SPR for spare parts."},
                    "quantity": {"type": "integer", "minimum": 1, "maximum": 1000, "description": "Quantity of the item, must be at least 1."},
                },
                "required": ["id", "itemType"],
                "additionalProperties": False,
            },
        },
        "retailId": {
            "type": "string",
            "minLength": 2,
            "maxLength": 10,
            "pattern": "^[A-Za-z]+$",
            "description": "Retail store identifier (letters only, no numbers)"
        },        
        "zipCode": {
            "type": "string",
            "pattern": "^[0-9]{5}$",
            "description": "5-digit postal code"
        }
    },
    "required": ["eligibleItems", "retailId", "zipCode"],
    "additionalProperties": False,
}

cart_details_input_schema = {
  "type": "object",
  "properties": {
    "cart_items": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "minLength": 1,
            "description": "Product name"
          },
          "sku": {
            "type": "string",
            "pattern": "^[A-Z0-9]+-[0-9]+$",
            "description": "Stock Keeping Unit, e.g., FURN-001"
          },
          "id": {
            "type": "string",
            "minLength": 1,
            "description": "Product identifier (string to preserve leading zeros)"
          },
          "quantity": {
            "type": "integer",
            "minimum": 1,
            "description": "Quantity must be at least 1"
          },
          "itemType": {
            "type": "string",
            "enum": ["ART", "SERV", "KIT", "PART"],
            "description": "Type of the item"
          },
          "price": {
            "type": "number",
            "minimum": 0,
            "description": "Unit price of the product"
          }
        },
        "required": ["name", "sku", "id", "quantity", "itemType", "price"],
        "additionalProperties": False
      }
    }
  },
  "required": ["cart_items"],
  "additionalProperties": False
}

class CartItem(BaseModel):
    """Output schema for cart details."""
    name: str = Field(..., description="Product name")
    sku: str = Field(..., pattern=r"^[A-Z0-9]+-[0-9]+$", description="Stock Keeping Unit, e.g., FURN-001")
    id: str = Field(..., description="Product identifier (string to preserve leading zeros)")
    quantity: conint(ge=1) = Field(..., description="Quantity must be at least 1")
    itemType: Literal["ART", "SPR"] = Field(..., description="Type of the item")
    price: confloat(ge=0) = Field(0.0, description="Unit price of the product, defaults to 0.0 if missing")
    service_eligible: bool = Field(..., description="Indicates if the item is eligible for service")

    class Config:
        extra = "forbid"

class CartItemsOutput(BaseModel):
    cart_details: List[CartItem] = Field(..., description="List of items in the cart")

    class Config:
        extra = "forbid"
        json_schema_extra = {
            "example": {
                "cart_details": [
                    {
                        "product_id": 101,
                        "name": "Wireless Mouse",
                        "quantity": 2,
                        "price": 25.99,
                        "service_eligible": True
                    },
                    {
                        "product_id": 102,
                        "name": "Keyboard",
                        "quantity": 1,
                        "price": 45.50,
                        "service_eligible": False
                    }
                ]
            }
        }


# ============================================================
# 4️⃣ Export tool schemas for OpenAPI/LLM
# ============================================================

TOOL_SCHEMAS = {
    "list_products": {
        "input_schema": ListProductsInput.model_json_schema(),
        "output_schema": ListProductsOutput.model_json_schema()
    },
    "get_product_details": {
        "input_schema": GetProductDetailsInput.model_json_schema(),
        "output_schema": GetProductDetailsOutput.model_json_schema()
    },
    "fetch_service_prices": {
        "input_schema": FetchServicePricesInput.model_json_schema(),
        "output_schema": FetchServicePricesOutput.model_json_schema(),
    }
}