# SelectedHomeDeliveryServiceDto

It describes the selected delivery service and its related information such as delivery, time window, pick up point etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | iSOM provided time window identifier | [optional] 
**selected_home_deliveries** | [**List[SelectedHomeDeliveryDto]**](SelectedHomeDeliveryDto.md) | It represents the details of the selected home delivery | [optional] 

## Example

```python
from order_capture_client.models.selected_home_delivery_service_dto import SelectedHomeDeliveryServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedHomeDeliveryServiceDto from a JSON string
selected_home_delivery_service_dto_instance = SelectedHomeDeliveryServiceDto.from_json(json)
# print the JSON string representation of the object
print(SelectedHomeDeliveryServiceDto.to_json())

# convert the object into a dict
selected_home_delivery_service_dto_dict = selected_home_delivery_service_dto_instance.to_dict()
# create an instance of SelectedHomeDeliveryServiceDto from a dict
selected_home_delivery_service_dto_from_dict = SelectedHomeDeliveryServiceDto.from_dict(selected_home_delivery_service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


