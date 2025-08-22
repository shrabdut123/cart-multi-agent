# DisplayUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**unit_information** | [**UnitInformation**](UnitInformation.md) |  | [optional] 

## Example

```python
from salesitem_client.models.display_unit import DisplayUnit

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayUnit from a JSON string
display_unit_instance = DisplayUnit.from_json(json)
# print the JSON string representation of the object
print(DisplayUnit.to_json())

# convert the object into a dict
display_unit_dict = display_unit_instance.to_dict()
# create an instance of DisplayUnit from a dict
display_unit_from_dict = DisplayUnit.from_dict(display_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


