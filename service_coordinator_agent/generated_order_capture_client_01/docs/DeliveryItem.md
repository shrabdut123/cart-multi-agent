# DeliveryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**item_no** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**ship_node** | **str** |  | [optional] 
**exceptional_qty** | **bool** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_item import DeliveryItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryItem from a JSON string
delivery_item_instance = DeliveryItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryItem.to_json())

# convert the object into a dict
delivery_item_dict = delivery_item_instance.to_dict()
# create an instance of DeliveryItem from a dict
delivery_item_from_dict = DeliveryItem.from_dict(delivery_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


