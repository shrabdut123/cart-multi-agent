# DeliverySlotMetadataDto

Informational attribute that describes whether a slot has price deviation from base price and time zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | It describes the time zone | [optional] 
**has_price_deviation** | **bool** | It is true when there is a price deviation. Else, it will be false. This is relevant only if prime time price is enabled for a market | [optional] 

## Example

```python
from order_capture_client.models.delivery_slot_metadata_dto import DeliverySlotMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverySlotMetadataDto from a JSON string
delivery_slot_metadata_dto_instance = DeliverySlotMetadataDto.from_json(json)
# print the JSON string representation of the object
print(DeliverySlotMetadataDto.to_json())

# convert the object into a dict
delivery_slot_metadata_dto_dict = delivery_slot_metadata_dto_instance.to_dict()
# create an instance of DeliverySlotMetadataDto from a dict
delivery_slot_metadata_dto_from_dict = DeliverySlotMetadataDto.from_dict(delivery_slot_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


