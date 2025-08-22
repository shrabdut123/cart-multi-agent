# PatchItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_no** | **str** | An itemNo that is already part of the checkout during the checkout creation. It should not be a child item of SPR and patching of child items of a SPR are not allowed | [optional] 
**quantity** | **int** | The quantity of the item. It should not be higher than the existing one | [optional] 

## Example

```python
from order_capture_client.models.patch_item_request import PatchItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchItemRequest from a JSON string
patch_item_request_instance = PatchItemRequest.from_json(json)
# print the JSON string representation of the object
print(PatchItemRequest.to_json())

# convert the object into a dict
patch_item_request_dict = patch_item_request_instance.to_dict()
# create an instance of PatchItemRequest from a dict
patch_item_request_from_dict = PatchItemRequest.from_dict(patch_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


