# PickUpPointPriceDeltaDto

It is for future use

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oc_pupid** | **str** | It describes the order capture generated UUID for a pick up point. Consumer must use this in API | [optional] 
**name** | **str** | iSOM provided name for a pick up point | [optional] 
**price** | [**DeltaPriceDto**](DeltaPriceDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.pick_up_point_price_delta_dto import PickUpPointPriceDeltaDto

# TODO update the JSON string below
json = "{}"
# create an instance of PickUpPointPriceDeltaDto from a JSON string
pick_up_point_price_delta_dto_instance = PickUpPointPriceDeltaDto.from_json(json)
# print the JSON string representation of the object
print(PickUpPointPriceDeltaDto.to_json())

# convert the object into a dict
pick_up_point_price_delta_dto_dict = pick_up_point_price_delta_dto_instance.to_dict()
# create an instance of PickUpPointPriceDeltaDto from a dict
pick_up_point_price_delta_dto_from_dict = PickUpPointPriceDeltaDto.from_dict(pick_up_point_price_delta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


