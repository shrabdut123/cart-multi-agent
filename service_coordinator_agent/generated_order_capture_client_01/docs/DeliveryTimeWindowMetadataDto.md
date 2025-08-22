# DeliveryTimeWindowMetadataDto

It describes the time windows metadata for a given delivery i.e. capacity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_capacity** | **bool** | It describes the capacity value provided by source system | [optional] 
**cheapest_slot_id** | **str** | It describes the cheapest slot identifier. This is the order capture UUID of a closest pick up point in a solution | [optional] 

## Example

```python
from order_capture_client.models.delivery_time_window_metadata_dto import DeliveryTimeWindowMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryTimeWindowMetadataDto from a JSON string
delivery_time_window_metadata_dto_instance = DeliveryTimeWindowMetadataDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryTimeWindowMetadataDto.to_json())

# convert the object into a dict
delivery_time_window_metadata_dto_dict = delivery_time_window_metadata_dto_instance.to_dict()
# create an instance of DeliveryTimeWindowMetadataDto from a dict
delivery_time_window_metadata_dto_from_dict = DeliveryTimeWindowMetadataDto.from_dict(delivery_time_window_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


