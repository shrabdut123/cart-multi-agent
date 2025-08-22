# AvailabilityClassificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ItemAvailabilityClassification]**](ItemAvailabilityClassification.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**trace_id** | **str** | The unique ID connected to this specific request. Can be used by support to trace the error | [optional] 

## Example

```python
from salesitem_client.models.availability_classification_response import AvailabilityClassificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityClassificationResponse from a JSON string
availability_classification_response_instance = AvailabilityClassificationResponse.from_json(json)
# print the JSON string representation of the object
print(AvailabilityClassificationResponse.to_json())

# convert the object into a dict
availability_classification_response_dict = availability_classification_response_instance.to_dict()
# create an instance of AvailabilityClassificationResponse from a dict
availability_classification_response_from_dict = AvailabilityClassificationResponse.from_dict(availability_classification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


