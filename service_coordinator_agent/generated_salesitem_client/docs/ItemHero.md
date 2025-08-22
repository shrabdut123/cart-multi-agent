# ItemHero


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_key** | [**ItemKey**](ItemKey.md) |  | [optional] 
**name** | **str** |  | [optional] 
**upsell_arguments** | [**List[UpsellArgument]**](UpsellArgument.md) |  | [optional] 

## Example

```python
from salesitem_client.models.item_hero import ItemHero

# TODO update the JSON string below
json = "{}"
# create an instance of ItemHero from a JSON string
item_hero_instance = ItemHero.from_json(json)
# print the JSON string representation of the object
print(ItemHero.to_json())

# convert the object into a dict
item_hero_dict = item_hero_instance.to_dict()
# create an instance of ItemHero from a dict
item_hero_from_dict = ItemHero.from_dict(item_hero_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


