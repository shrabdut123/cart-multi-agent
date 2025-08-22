# Error

It describes the time window error for a given delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**solution_id** | **str** |  | [optional] 
**pick_up_point_data** | **List[str]** |  | [optional] 
**error_detail** | [**ErrorDetail**](ErrorDetail.md) |  | [optional] 

## Example

```python
from order_capture_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


