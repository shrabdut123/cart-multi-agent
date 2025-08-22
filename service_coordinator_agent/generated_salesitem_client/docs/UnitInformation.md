# UnitInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_imperial** | **str** |  | [optional] 
**unit_imperial_value** | **str** |  | [optional] 
**unit_metric** | **str** |  | [optional] 
**unit_metric_value** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.unit_information import UnitInformation

# TODO update the JSON string below
json = "{}"
# create an instance of UnitInformation from a JSON string
unit_information_instance = UnitInformation.from_json(json)
# print the JSON string representation of the object
print(UnitInformation.to_json())

# convert the object into a dict
unit_information_dict = unit_information_instance.to_dict()
# create an instance of UnitInformation from a dict
unit_information_from_dict = UnitInformation.from_dict(unit_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


