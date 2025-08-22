# ItemReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_line_id** | **str** |  | [optional] 
**item_no** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**is_co_worker_assistance_needed** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.item_reference import ItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReference from a JSON string
item_reference_instance = ItemReference.from_json(json)
# print the JSON string representation of the object
print(ItemReference.to_json())

# convert the object into a dict
item_reference_dict = item_reference_instance.to_dict()
# create an instance of ItemReference from a dict
item_reference_from_dict = ItemReference.from_dict(item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


