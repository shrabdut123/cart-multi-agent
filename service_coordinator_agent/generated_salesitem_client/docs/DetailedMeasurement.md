# DetailedMeasurement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_imperial** | **str** |  | [optional] 
**text_metric** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.detailed_measurement import DetailedMeasurement

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedMeasurement from a JSON string
detailed_measurement_instance = DetailedMeasurement.from_json(json)
# print the JSON string representation of the object
print(DetailedMeasurement.to_json())

# convert the object into a dict
detailed_measurement_dict = detailed_measurement_instance.to_dict()
# create an instance of DetailedMeasurement from a dict
detailed_measurement_from_dict = DetailedMeasurement.from_dict(detailed_measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


