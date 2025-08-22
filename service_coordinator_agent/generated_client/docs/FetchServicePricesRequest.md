# FetchServicePricesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | GraphQL query string | [optional] 
**variables** | **Dict[str, object]** | Optional variables for the query | [optional] 

## Example

```python
from openapi_client.models.fetch_service_prices_request import FetchServicePricesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchServicePricesRequest from a JSON string
fetch_service_prices_request_instance = FetchServicePricesRequest.from_json(json)
# print the JSON string representation of the object
print(FetchServicePricesRequest.to_json())

# convert the object into a dict
fetch_service_prices_request_dict = fetch_service_prices_request_instance.to_dict()
# create an instance of FetchServicePricesRequest from a dict
fetch_service_prices_request_from_dict = FetchServicePricesRequest.from_dict(fetch_service_prices_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


