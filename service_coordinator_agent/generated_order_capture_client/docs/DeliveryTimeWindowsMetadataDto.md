# DeliveryTimeWindowsMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_slot_price** | **float** | It describes the maximum possible slot price among all the available time windows, in case of split delivery, this will show the max(max of each TW slots price) | [optional] 
**min_slot_price** | **float** | It describes the minimum possible slot price among all the available time windows, in case of split delivery, this will show the max(min of each TW slots price) | [optional] 

## Example

```python
from order_capture_client.models.delivery_time_windows_metadata_dto import DeliveryTimeWindowsMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryTimeWindowsMetadataDto from a JSON string
delivery_time_windows_metadata_dto_instance = DeliveryTimeWindowsMetadataDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryTimeWindowsMetadataDto.to_json())

# convert the object into a dict
delivery_time_windows_metadata_dto_dict = delivery_time_windows_metadata_dto_instance.to_dict()
# create an instance of DeliveryTimeWindowsMetadataDto from a dict
delivery_time_windows_metadata_dto_from_dict = DeliveryTimeWindowsMetadataDto.from_dict(delivery_time_windows_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


