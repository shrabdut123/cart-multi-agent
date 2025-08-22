# DeliveryEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**fulfillment_delivery_id** | **str** |  | [optional] 
**service_item_id** | **str** |  | [optional] 
**range_of_days** | **bool** |  | [optional] 
**ship_node** | **str** |  | [optional] 
**merge_node_list** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 
**delivery_price** | [**Price**](Price.md) |  | [optional] 
**price_override_reference** | **float** |  | [optional] 
**delivery_items** | [**List[DeliveryItem]**](DeliveryItem.md) |  | [optional] 
**selected_pick_up_point** | [**PickUpPointEntity**](PickUpPointEntity.md) |  | [optional] 
**selected_slot** | [**DeliverySlot**](DeliverySlot.md) |  | [optional] 
**taxation_info** | **str** |  | [optional] 
**is_exceptional_qty** | **bool** |  | [optional] 
**is_exceptional_volume** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_entity import DeliveryEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryEntity from a JSON string
delivery_entity_instance = DeliveryEntity.from_json(json)
# print the JSON string representation of the object
print(DeliveryEntity.to_json())

# convert the object into a dict
delivery_entity_dict = delivery_entity_instance.to_dict()
# create an instance of DeliveryEntity from a dict
delivery_entity_from_dict = DeliveryEntity.from_dict(delivery_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


