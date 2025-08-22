# PossiblePickUpPointsDto

This node is available only if the delivery service fulfillment type is COLLECT. This node wraps the pickup point metadata along with list of pick up points for a delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**possible_pick_up_point_metadata** | [**PossiblePickUpPointMetadataDto**](PossiblePickUpPointMetadataDto.md) |  | [optional] 
**pick_up_points** | [**List[PickUpPointDto]**](PickUpPointDto.md) | List of possible pick up points with details | [optional] 

## Example

```python
from order_capture_client.models.possible_pick_up_points_dto import PossiblePickUpPointsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossiblePickUpPointsDto from a JSON string
possible_pick_up_points_dto_instance = PossiblePickUpPointsDto.from_json(json)
# print the JSON string representation of the object
print(PossiblePickUpPointsDto.to_json())

# convert the object into a dict
possible_pick_up_points_dto_dict = possible_pick_up_points_dto_instance.to_dict()
# create an instance of PossiblePickUpPointsDto from a dict
possible_pick_up_points_dto_from_dict = PossiblePickUpPointsDto.from_dict(possible_pick_up_points_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


