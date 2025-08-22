# DeliverySlotOfTargetHDDto

It represents the earliestSlot of the target delivery with calculated delta price values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | iSOM provided time window identifier | [optional] 
**from_date_time** | **str** | The start date and time of a slot. This is already adjusted to delivery zip code time zone and it is an information from iSOM | [optional] 
**to_date_time** | **str** | The end date and time of a slot. This is already adjusted to delivery zip code time zone and it is an information from iSOM | [optional] 
**price** | [**DeltaPriceDto**](DeltaPriceDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_slot_of_target_hd_dto import DeliverySlotOfTargetHDDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverySlotOfTargetHDDto from a JSON string
delivery_slot_of_target_hd_dto_instance = DeliverySlotOfTargetHDDto.from_json(json)
# print the JSON string representation of the object
print(DeliverySlotOfTargetHDDto.to_json())

# convert the object into a dict
delivery_slot_of_target_hd_dto_dict = delivery_slot_of_target_hd_dto_instance.to_dict()
# create an instance of DeliverySlotOfTargetHDDto from a dict
delivery_slot_of_target_hd_dto_from_dict = DeliverySlotOfTargetHDDto.from_dict(delivery_slot_of_target_hd_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


