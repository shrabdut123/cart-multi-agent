# ExperimentalItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the experiment, e.g. \&quot;teamname-testname\&quot; | [optional] 
**data** | **str** | JSON-encoded data for the feature | [optional] 

## Example

```python
from salesitem_client.models.experimental_item import ExperimentalItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalItem from a JSON string
experimental_item_instance = ExperimentalItem.from_json(json)
# print the JSON string representation of the object
print(ExperimentalItem.to_json())

# convert the object into a dict
experimental_item_dict = experimental_item_instance.to_dict()
# create an instance of ExperimentalItem from a dict
experimental_item_from_dict = ExperimentalItem.from_dict(experimental_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


