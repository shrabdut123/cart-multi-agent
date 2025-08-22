# DeliverySlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DeliverySlotMetadata**](DeliverySlotMetadata.md) |  | [optional] 
**id** | **str** |  | [optional] 
**from_date_time** | **str** |  | [optional] 
**to_date_time** | **str** |  | [optional] 
**node** | **str** |  | [optional] 
**resource_pool_id** | **str** |  | [optional] 
**tsp_id** | **str** |  | [optional] 
**tsp_name** | **str** |  | [optional] 
**slot_attribute_group** | **str** |  | [optional] 
**capability** | [**List[DeliverySlotCapability]**](DeliverySlotCapability.md) |  | [optional] 
**price** | [**SlotPrice**](SlotPrice.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_slot import DeliverySlot

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverySlot from a JSON string
delivery_slot_instance = DeliverySlot.from_json(json)
# print the JSON string representation of the object
print(DeliverySlot.to_json())

# convert the object into a dict
delivery_slot_dict = delivery_slot_instance.to_dict()
# create an instance of DeliverySlot from a dict
delivery_slot_from_dict = DeliverySlot.from_dict(delivery_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


