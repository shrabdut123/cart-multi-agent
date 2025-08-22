# ErrorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**details_map** | **Dict[str, str]** |  | [optional] 
**error_code** | **int** |  | [optional] 
**ga_error** | [**GaError**](GaError.md) |  | [optional] 
**ga_error_list** | [**List[GaError]**](GaError.md) |  | [optional] 

## Example

```python
from order_capture_client.models.error_details import ErrorDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetails from a JSON string
error_details_instance = ErrorDetails.from_json(json)
# print the JSON string representation of the object
print(ErrorDetails.to_json())

# convert the object into a dict
error_details_dict = error_details_instance.to_dict()
# create an instance of ErrorDetails from a dict
error_details_from_dict = ErrorDetails.from_dict(error_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


