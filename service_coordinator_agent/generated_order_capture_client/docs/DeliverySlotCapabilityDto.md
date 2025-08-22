# DeliverySlotCapabilityDto

It describes the capability for a slot. An example is whether this slot is available for contactless delivery i.e. Authority to leave goods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | It describes the capability for a slot. An example is whether this slot is available for contactless delivery i.e. Authority to leave goods | [optional] 

## Example

```python
from order_capture_client.models.delivery_slot_capability_dto import DeliverySlotCapabilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverySlotCapabilityDto from a JSON string
delivery_slot_capability_dto_instance = DeliverySlotCapabilityDto.from_json(json)
# print the JSON string representation of the object
print(DeliverySlotCapabilityDto.to_json())

# convert the object into a dict
delivery_slot_capability_dto_dict = delivery_slot_capability_dto_instance.to_dict()
# create an instance of DeliverySlotCapabilityDto from a dict
delivery_slot_capability_dto_from_dict = DeliverySlotCapabilityDto.from_dict(delivery_slot_capability_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


