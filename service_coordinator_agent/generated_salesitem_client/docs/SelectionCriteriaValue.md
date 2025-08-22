# SelectionCriteriaValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_keys** | [**List[ItemKey]**](ItemKey.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.selection_criteria_value import SelectionCriteriaValue

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionCriteriaValue from a JSON string
selection_criteria_value_instance = SelectionCriteriaValue.from_json(json)
# print the JSON string representation of the object
print(SelectionCriteriaValue.to_json())

# convert the object into a dict
selection_criteria_value_dict = selection_criteria_value_instance.to_dict()
# create an instance of SelectionCriteriaValue from a dict
selection_criteria_value_from_dict = SelectionCriteriaValue.from_dict(selection_criteria_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


