# ReferenceMeasurementFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imperial** | **str** |  | [optional] 
**metric** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.reference_measurement_filter import ReferenceMeasurementFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceMeasurementFilter from a JSON string
reference_measurement_filter_instance = ReferenceMeasurementFilter.from_json(json)
# print the JSON string representation of the object
print(ReferenceMeasurementFilter.to_json())

# convert the object into a dict
reference_measurement_filter_dict = reference_measurement_filter_instance.to_dict()
# create an instance of ReferenceMeasurementFilter from a dict
reference_measurement_filter_from_dict = ReferenceMeasurementFilter.from_dict(reference_measurement_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


