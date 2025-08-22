# MeasurementFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_imperial** | **str** |  | [optional] 
**text_metric** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**unit_imperial** | **str** |  | [optional] 
**unit_metric** | **str** |  | [optional] 
**value_imperial** | **str** |  | [optional] 
**value_metric** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.measurement_filter import MeasurementFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementFilter from a JSON string
measurement_filter_instance = MeasurementFilter.from_json(json)
# print the JSON string representation of the object
print(MeasurementFilter.to_json())

# convert the object into a dict
measurement_filter_dict = measurement_filter_instance.to_dict()
# create an instance of MeasurementFilter from a dict
measurement_filter_from_dict = MeasurementFilter.from_dict(measurement_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


