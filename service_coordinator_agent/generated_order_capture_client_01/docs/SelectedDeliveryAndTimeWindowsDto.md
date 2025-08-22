# SelectedDeliveryAndTimeWindowsDto

It refers to details related to selected time window and pick up point if it is collect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **str** | It refers to the delivery id under a selected delivery service | 
**pick_up_point_id** | **str** | The selected pick up point of above delivery if the selected delivery service is a collect delivery | [optional] 
**time_window_id** | **str** | The selected time window ID of the above delivery | 
**capabilities** | [**SelectedCapabilityDto**](SelectedCapabilityDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.selected_delivery_and_time_windows_dto import SelectedDeliveryAndTimeWindowsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedDeliveryAndTimeWindowsDto from a JSON string
selected_delivery_and_time_windows_dto_instance = SelectedDeliveryAndTimeWindowsDto.from_json(json)
# print the JSON string representation of the object
print(SelectedDeliveryAndTimeWindowsDto.to_json())

# convert the object into a dict
selected_delivery_and_time_windows_dto_dict = selected_delivery_and_time_windows_dto_instance.to_dict()
# create an instance of SelectedDeliveryAndTimeWindowsDto from a dict
selected_delivery_and_time_windows_dto_from_dict = SelectedDeliveryAndTimeWindowsDto.from_dict(selected_delivery_and_time_windows_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


