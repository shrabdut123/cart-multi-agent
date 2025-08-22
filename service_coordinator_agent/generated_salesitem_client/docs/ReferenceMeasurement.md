# ReferenceMeasurement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imperial** | **str** |  | [optional] 
**metric** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.reference_measurement import ReferenceMeasurement

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceMeasurement from a JSON string
reference_measurement_instance = ReferenceMeasurement.from_json(json)
# print the JSON string representation of the object
print(ReferenceMeasurement.to_json())

# convert the object into a dict
reference_measurement_dict = reference_measurement_instance.to_dict()
# create an instance of ReferenceMeasurement from a dict
reference_measurement_from_dict = ReferenceMeasurement.from_dict(reference_measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


