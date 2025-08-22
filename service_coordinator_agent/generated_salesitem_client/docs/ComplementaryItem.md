# ComplementaryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_key** | [**ItemKey**](ItemKey.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.complementary_item import ComplementaryItem

# TODO update the JSON string below
json = "{}"
# create an instance of ComplementaryItem from a JSON string
complementary_item_instance = ComplementaryItem.from_json(json)
# print the JSON string representation of the object
print(ComplementaryItem.to_json())

# convert the object into a dict
complementary_item_dict = complementary_item_instance.to_dict()
# create an instance of ComplementaryItem from a dict
complementary_item_from_dict = ComplementaryItem.from_dict(complementary_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


