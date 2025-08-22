# SelectedDeliveryAndServiceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | It is the type of delivery | 
**selected_delivery_service** | [**SelectedDeliveryServiceDto**](SelectedDeliveryServiceDto.md) |  | 
**selected_services** | [**List[SelectedServiceDto]**](SelectedServiceDto.md) | It describes the active services and it&#39;s time windows. It should be provided if the are at least one active service in the checkout | [optional] 
**services_with_time_window_errors** | [**List[ServiceTimeWindowErrorDto]**](ServiceTimeWindowErrorDto.md) | It describes the list of services that has service time window failures | [optional] 
**service_time_windows_failure_exist** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.selected_delivery_and_service_request_dto import SelectedDeliveryAndServiceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedDeliveryAndServiceRequestDto from a JSON string
selected_delivery_and_service_request_dto_instance = SelectedDeliveryAndServiceRequestDto.from_json(json)
# print the JSON string representation of the object
print(SelectedDeliveryAndServiceRequestDto.to_json())

# convert the object into a dict
selected_delivery_and_service_request_dto_dict = selected_delivery_and_service_request_dto_instance.to_dict()
# create an instance of SelectedDeliveryAndServiceRequestDto from a dict
selected_delivery_and_service_request_dto_from_dict = SelectedDeliveryAndServiceRequestDto.from_dict(selected_delivery_and_service_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


