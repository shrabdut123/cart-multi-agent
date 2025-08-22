# SelectedDeliveryServiceDto

It describes the selected delivery service and its related information such as delivery, time window, pick up point etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_service_id** | **str** | It refers to the selected delivery service ID | 
**delivery_and_time_windows** | [**List[SelectedDeliveryAndTimeWindowsDto]**](SelectedDeliveryAndTimeWindowsDto.md) | It refers to details related to selected time window and pick up point if it is collect | 

## Example

```python
from order_capture_client.models.selected_delivery_service_dto import SelectedDeliveryServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedDeliveryServiceDto from a JSON string
selected_delivery_service_dto_instance = SelectedDeliveryServiceDto.from_json(json)
# print the JSON string representation of the object
print(SelectedDeliveryServiceDto.to_json())

# convert the object into a dict
selected_delivery_service_dto_dict = selected_delivery_service_dto_instance.to_dict()
# create an instance of SelectedDeliveryServiceDto from a dict
selected_delivery_service_dto_from_dict = SelectedDeliveryServiceDto.from_dict(selected_delivery_service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


