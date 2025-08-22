# SelectedHomeDeliveryDto

It represents the details of the selected home delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **str** | iSOM provided time window identifier | [optional] 
**selected_time_window_id** | **str** | It represents the timewindow Id of the selected delivery | [optional] 
**selected_time_window_price** | [**SlotPrice**](SlotPrice.md) |  | [optional] 

## Example

```python
from order_capture_client.models.selected_home_delivery_dto import SelectedHomeDeliveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedHomeDeliveryDto from a JSON string
selected_home_delivery_dto_instance = SelectedHomeDeliveryDto.from_json(json)
# print the JSON string representation of the object
print(SelectedHomeDeliveryDto.to_json())

# convert the object into a dict
selected_home_delivery_dto_dict = selected_home_delivery_dto_instance.to_dict()
# create an instance of SelectedHomeDeliveryDto from a dict
selected_home_delivery_dto_from_dict = SelectedHomeDeliveryDto.from_dict(selected_home_delivery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


