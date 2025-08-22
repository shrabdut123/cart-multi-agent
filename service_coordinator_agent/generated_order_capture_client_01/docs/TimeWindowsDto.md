# TimeWindowsDto

This node is available when fulfillment type is HOME_DELIVERY. This contains the information of when a delivery is possible. For COLLECT, time window should be looked under each pick up point

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**TimeWindowMetadataDto**](TimeWindowMetadataDto.md) |  | [optional] 
**earliest_possible_slot** | [**DeliverySlotDto**](DeliverySlotDto.md) |  | [optional] 
**error** | [**ErrorDto**](ErrorDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.time_windows_dto import TimeWindowsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimeWindowsDto from a JSON string
time_windows_dto_instance = TimeWindowsDto.from_json(json)
# print the JSON string representation of the object
print(TimeWindowsDto.to_json())

# convert the object into a dict
time_windows_dto_dict = time_windows_dto_instance.to_dict()
# create an instance of TimeWindowsDto from a dict
time_windows_dto_from_dict = TimeWindowsDto.from_dict(time_windows_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


