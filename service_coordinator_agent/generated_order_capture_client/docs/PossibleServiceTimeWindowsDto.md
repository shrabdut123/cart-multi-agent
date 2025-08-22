# PossibleServiceTimeWindowsDto

It describes the available time slots for services present in request. It wraps the time window information with additional supporting data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_delivery_solution** | [**STWSelectedDSDto**](STWSelectedDSDto.md) |  | [optional] 
**service_time_windows** | [**List[PossibleServiceTimeWindowDto]**](PossibleServiceTimeWindowDto.md) | It describes the time windows for each service that was added in cart and active i.e. supported by the service and other parameters such as co-worker assistance | [optional] 

## Example

```python
from order_capture_client.models.possible_service_time_windows_dto import PossibleServiceTimeWindowsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleServiceTimeWindowsDto from a JSON string
possible_service_time_windows_dto_instance = PossibleServiceTimeWindowsDto.from_json(json)
# print the JSON string representation of the object
print(PossibleServiceTimeWindowsDto.to_json())

# convert the object into a dict
possible_service_time_windows_dto_dict = possible_service_time_windows_dto_instance.to_dict()
# create an instance of PossibleServiceTimeWindowsDto from a dict
possible_service_time_windows_dto_from_dict = PossibleServiceTimeWindowsDto.from_dict(possible_service_time_windows_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


