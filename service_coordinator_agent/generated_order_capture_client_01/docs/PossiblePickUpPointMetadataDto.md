# PossiblePickUpPointMetadataDto

It describes informational metadata i.e. closestPickUpPointId as an example

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closest_pick_up_point_id** | **str** | It is the order capture generated PUP identifier of a closest pick up point | [optional] 

## Example

```python
from order_capture_client.models.possible_pick_up_point_metadata_dto import PossiblePickUpPointMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossiblePickUpPointMetadataDto from a JSON string
possible_pick_up_point_metadata_dto_instance = PossiblePickUpPointMetadataDto.from_json(json)
# print the JSON string representation of the object
print(PossiblePickUpPointMetadataDto.to_json())

# convert the object into a dict
possible_pick_up_point_metadata_dto_dict = possible_pick_up_point_metadata_dto_instance.to_dict()
# create an instance of PossiblePickUpPointMetadataDto from a dict
possible_pick_up_point_metadata_dto_from_dict = PossiblePickUpPointMetadataDto.from_dict(possible_pick_up_point_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


