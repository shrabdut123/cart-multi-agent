# GenericProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GenericProductCommunication]**](GenericProductCommunication.md) |  | 
**error** | [**Status**](Status.md) |  | [optional] 
**trace_id** | **str** | The unique ID connected to this specific request. Can be used by support to trace the error | [optional] 

## Example

```python
from salesitem_client.models.generic_product_response import GenericProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenericProductResponse from a JSON string
generic_product_response_instance = GenericProductResponse.from_json(json)
# print the JSON string representation of the object
print(GenericProductResponse.to_json())

# convert the object into a dict
generic_product_response_dict = generic_product_response_instance.to_dict()
# create an instance of GenericProductResponse from a dict
generic_product_response_from_dict = GenericProductResponse.from_dict(generic_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


