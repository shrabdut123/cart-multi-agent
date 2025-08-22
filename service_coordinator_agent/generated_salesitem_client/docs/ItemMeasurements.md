# ItemMeasurements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailed_measurements** | [**List[DetailedMeasurement]**](DetailedMeasurement.md) |  | [optional] 
**reference_measurements** | [**List[ReferenceMeasurement]**](ReferenceMeasurement.md) |  | [optional] 

## Example

```python
from salesitem_client.models.item_measurements import ItemMeasurements

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMeasurements from a JSON string
item_measurements_instance = ItemMeasurements.from_json(json)
# print the JSON string representation of the object
print(ItemMeasurements.to_json())

# convert the object into a dict
item_measurements_dict = item_measurements_instance.to_dict()
# create an instance of ItemMeasurements from a dict
item_measurements_from_dict = ItemMeasurements.from_dict(item_measurements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


