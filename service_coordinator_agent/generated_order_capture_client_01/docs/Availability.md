# Availability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**unavailability_reason** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.availability import Availability

# TODO update the JSON string below
json = "{}"
# create an instance of Availability from a JSON string
availability_instance = Availability.from_json(json)
# print the JSON string representation of the object
print(Availability.to_json())

# convert the object into a dict
availability_dict = availability_instance.to_dict()
# create an instance of Availability from a dict
availability_from_dict = Availability.from_dict(availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


