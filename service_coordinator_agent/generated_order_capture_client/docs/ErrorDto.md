# ErrorDto

It contains a list of different errors that could possibly impact this as a choice of selection. The metadata has information that helps decide the presentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | It describes the kind of error whether it is an application, system, communication or an internal order capture error | [optional] 
**service** | **str** | It describes the external interaction that was impacted. If internal, then it will be internal mapping | [optional] 
**solution_id** | **str** | It describes the iSOM solution ID that has an error | [optional] 
**pick_up_point_data** | **List[str]** | It describes the list of pick up points that are affected by this error | [optional] 
**error_detail** | [**ErrorDetailDto**](ErrorDetailDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.error_dto import ErrorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDto from a JSON string
error_dto_instance = ErrorDto.from_json(json)
# print the JSON string representation of the object
print(ErrorDto.to_json())

# convert the object into a dict
error_dto_dict = error_dto_instance.to_dict()
# create an instance of ErrorDto from a dict
error_dto_from_dict = ErrorDto.from_dict(error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


