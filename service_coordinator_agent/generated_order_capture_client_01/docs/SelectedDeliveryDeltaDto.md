# SelectedDeliveryDeltaDto

It represents the list of selected delivery details in case of split

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **str** | It represents the selected delivery Id in the split delivery | [optional] 
**selected_pick_up_point** | [**SelectedPUPPriceDeltaDto**](SelectedPUPPriceDeltaDto.md) |  | [optional] 
**selected_time_window_id** | **str** | It represents the timewindow Id of the selected delivery | [optional] 

## Example

```python
from order_capture_client.models.selected_delivery_delta_dto import SelectedDeliveryDeltaDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedDeliveryDeltaDto from a JSON string
selected_delivery_delta_dto_instance = SelectedDeliveryDeltaDto.from_json(json)
# print the JSON string representation of the object
print(SelectedDeliveryDeltaDto.to_json())

# convert the object into a dict
selected_delivery_delta_dto_dict = selected_delivery_delta_dto_instance.to_dict()
# create an instance of SelectedDeliveryDeltaDto from a dict
selected_delivery_delta_dto_from_dict = SelectedDeliveryDeltaDto.from_dict(selected_delivery_delta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


