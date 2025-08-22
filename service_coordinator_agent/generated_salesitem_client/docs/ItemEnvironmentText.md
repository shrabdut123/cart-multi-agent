# ItemEnvironmentText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type_text** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_environment_text import ItemEnvironmentText

# TODO update the JSON string below
json = "{}"
# create an instance of ItemEnvironmentText from a JSON string
item_environment_text_instance = ItemEnvironmentText.from_json(json)
# print the JSON string representation of the object
print(ItemEnvironmentText.to_json())

# convert the object into a dict
item_environment_text_dict = item_environment_text_instance.to_dict()
# create an instance of ItemEnvironmentText from a dict
item_environment_text_from_dict = ItemEnvironmentText.from_dict(item_environment_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


