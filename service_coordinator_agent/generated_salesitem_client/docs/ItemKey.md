# ItemKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_no** | **str** | The number of the item. Identifies an IKEA item together with the type. | 
**item_type** | **str** | Type of the Item, e.g. &#39;ART&#39;, &#39;SPR&#39;, &#39;SGR&#39;. | 

## Example

```python
from salesitem_client.models.item_key import ItemKey

# TODO update the JSON string below
json = "{}"
# create an instance of ItemKey from a JSON string
item_key_instance = ItemKey.from_json(json)
# print the JSON string representation of the object
print(ItemKey.to_json())

# convert the object into a dict
item_key_dict = item_key_instance.to_dict()
# create an instance of ItemKey from a dict
item_key_from_dict = ItemKey.from_dict(item_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


