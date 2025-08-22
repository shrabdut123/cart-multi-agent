# LastChance

Deprecated - use productTags instead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** | Is the item considered last chance according to RPIM API | [optional] 

## Example

```python
from salesitem_client.models.last_chance import LastChance

# TODO update the JSON string below
json = "{}"
# create an instance of LastChance from a JSON string
last_chance_instance = LastChance.from_json(json)
# print the JSON string representation of the object
print(LastChance.to_json())

# convert the object into a dict
last_chance_dict = last_chance_instance.to_dict()
# create an instance of LastChance from a dict
last_chance_from_dict = LastChance.from_dict(last_chance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


