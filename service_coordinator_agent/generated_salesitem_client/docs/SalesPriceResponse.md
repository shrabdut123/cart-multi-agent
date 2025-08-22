# SalesPriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ItemSalesPrice]**](ItemSalesPrice.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**trace_id** | **str** | The unique ID connected to this specific request. Can be used by support to trace the error | [optional] 

## Example

```python
from salesitem_client.models.sales_price_response import SalesPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SalesPriceResponse from a JSON string
sales_price_response_instance = SalesPriceResponse.from_json(json)
# print the JSON string representation of the object
print(SalesPriceResponse.to_json())

# convert the object into a dict
sales_price_response_dict = sales_price_response_instance.to_dict()
# create an instance of SalesPriceResponse from a dict
sales_price_response_from_dict = SalesPriceResponse.from_dict(sales_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


