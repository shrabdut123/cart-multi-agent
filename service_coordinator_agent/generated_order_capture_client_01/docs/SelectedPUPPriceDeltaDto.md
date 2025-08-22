# SelectedPUPPriceDeltaDto

It represents the price details of the selected PUP in the split delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oc_pupid** | **str** | It describes the order capture generated UUID for a pick up point. Consumer must use this in API | [optional] 
**name** | **str** | iSOM provided name for a pick up point | [optional] 
**price** | [**PUPPrice**](PUPPrice.md) |  | [optional] 

## Example

```python
from order_capture_client.models.selected_pup_price_delta_dto import SelectedPUPPriceDeltaDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedPUPPriceDeltaDto from a JSON string
selected_pup_price_delta_dto_instance = SelectedPUPPriceDeltaDto.from_json(json)
# print the JSON string representation of the object
print(SelectedPUPPriceDeltaDto.to_json())

# convert the object into a dict
selected_pup_price_delta_dto_dict = selected_pup_price_delta_dto_instance.to_dict()
# create an instance of SelectedPUPPriceDeltaDto from a dict
selected_pup_price_delta_dto_from_dict = SelectedPUPPriceDeltaDto.from_dict(selected_pup_price_delta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


