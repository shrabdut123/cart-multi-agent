# FilterInformation

Populated by information coming from the Retail PIM Product Data Harmonizer component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_filters** | [**List[ClassFilter]**](ClassFilter.md) |  | [optional] 
**measurement_filters** | [**List[MeasurementFilter]**](MeasurementFilter.md) |  | [optional] 
**reference_measurement_filter** | [**ReferenceMeasurementFilter**](ReferenceMeasurementFilter.md) |  | [optional] 

## Example

```python
from salesitem_client.models.filter_information import FilterInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FilterInformation from a JSON string
filter_information_instance = FilterInformation.from_json(json)
# print the JSON string representation of the object
print(FilterInformation.to_json())

# convert the object into a dict
filter_information_dict = filter_information_instance.to_dict()
# create an instance of FilterInformation from a dict
filter_information_from_dict = FilterInformation.from_dict(filter_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


