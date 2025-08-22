# ItemReferenceRequest

It refers to the items for which the service is requested

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_no** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**is_co_worker_assistance_needed** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.item_reference_request import ItemReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReferenceRequest from a JSON string
item_reference_request_instance = ItemReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(ItemReferenceRequest.to_json())

# convert the object into a dict
item_reference_request_dict = item_reference_request_instance.to_dict()
# create an instance of ItemReferenceRequest from a dict
item_reference_request_from_dict = ItemReferenceRequest.from_dict(item_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


