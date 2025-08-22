# DeliverySlotDto

It describes the slot for a delivery service which contains from and to time with few additional info

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DeliverySlotMetadataDto**](DeliverySlotMetadataDto.md) |  | [optional] 
**id** | **str** | iSOM provided time window identifier | [optional] 
**from_date_time** | **str** | The start date and time of a slot. This is already adjusted to delivery zip code time zone and it is an information from iSOM | [optional] 
**to_date_time** | **str** | The end date and time of a slot. This is already adjusted to delivery zip code time zone and it is an information from iSOM | [optional] 
**capability** | [**List[DeliverySlotCapabilityDto]**](DeliverySlotCapabilityDto.md) | It describes the capability for a slot. An example is whether this slot is available for contactless delivery i.e. Authority to leave goods | [optional] 
**price** | [**SlotPrice**](SlotPrice.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_slot_dto import DeliverySlotDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverySlotDto from a JSON string
delivery_slot_dto_instance = DeliverySlotDto.from_json(json)
# print the JSON string representation of the object
print(DeliverySlotDto.to_json())

# convert the object into a dict
delivery_slot_dto_dict = delivery_slot_dto_instance.to_dict()
# create an instance of DeliverySlotDto from a dict
delivery_slot_dto_from_dict = DeliverySlotDto.from_dict(delivery_slot_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


