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
    print("Response from service prices API:", response)
    response.raise_for_status()
    data = response.json()
    pricing_info = data.get("data", {}).get("servicePrices", {}).get("SGR50000960", {})
    print("Parsed pricing info:", pricing_info)
    pricing_items = pricing_info.get("items", [])
    print("Pricing items:", pricing_items)
    configuration = pricing_info.get("configuration", {})
    print("Configuration:", configuration)
    return {
        "items": pricing_items,
        "configuration": configuration
    }
  
