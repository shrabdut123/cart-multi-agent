# GaError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.ga_error import GaError

# TODO update the JSON string below
json = "{}"
# create an instance of GaError from a JSON string
ga_error_instance = GaError.from_json(json)
# print the JSON string representation of the object
print(GaError.to_json())

# convert the object into a dict
ga_error_dict = ga_error_instance.to_dict()
# create an instance of GaError from a dict
ga_error_from_dict = GaError.from_dict(ga_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


