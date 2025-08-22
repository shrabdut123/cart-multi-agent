# SelectionCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** |  | [optional] 
**type_name_global** | **str** |  | [optional] 
**type_no** | **str** |  | [optional] 
**values** | [**List[SelectionCriteriaValue]**](SelectionCriteriaValue.md) |  | [optional] 

## Example

```python
from salesitem_client.models.selection_criteria import SelectionCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionCriteria from a JSON string
selection_criteria_instance = SelectionCriteria.from_json(json)
# print the JSON string representation of the object
print(SelectionCriteria.to_json())

# convert the object into a dict
selection_criteria_dict = selection_criteria_instance.to_dict()
# create an instance of SelectionCriteria from a dict
selection_criteria_from_dict = SelectionCriteria.from_dict(selection_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


