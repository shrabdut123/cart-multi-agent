# SelectedDeliveryServiceDeltaDto

It describes the selected delivery service and its related information such as delivery, time window, pick up point etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | It refers to the delivery id under a selected delivery service | [optional] 
**deliveries** | [**List[SelectedDeliveryDeltaDto]**](SelectedDeliveryDeltaDto.md) | It represents the list of selected delivery details in case of split | [optional] 

## Example

```python
from order_capture_client.models.selected_delivery_service_delta_dto import SelectedDeliveryServiceDeltaDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedDeliveryServiceDeltaDto from a JSON string
selected_delivery_service_delta_dto_instance = SelectedDeliveryServiceDeltaDto.from_json(json)
# print the JSON string representation of the object
print(SelectedDeliveryServiceDeltaDto.to_json())

# convert the object into a dict
selected_delivery_service_delta_dto_dict = selected_delivery_service_delta_dto_instance.to_dict()
# create an instance of SelectedDeliveryServiceDeltaDto from a dict
selected_delivery_service_delta_dto_from_dict = SelectedDeliveryServiceDeltaDto.from_dict(selected_delivery_service_delta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


