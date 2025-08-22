# ItemChild

By default only `itemKey` and `quantity` is returned. Use the query parameter `expand` with a value of `ChildItems` to get complete information for all child items. E.g. `GET https://api.salesitem.ingka.com/communications/ru/gb?itemNos=19278540&languageCode=en&expand=ChildItems`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_ons** | [**List[AddOn]**](AddOn.md) |  | [optional] 
**business_structure** | [**BusinessStructure**](BusinessStructure.md) |  | [optional] 
**complementary_items** | [**List[ComplementaryItem]**](ComplementaryItem.md) |  | [optional] 
**filter_classes** | **List[str]** |  | [optional] 
**is_assembly_required** | **bool** |  | [optional] 
**is_breath_taking_item** | **bool** | Deprecated - use productTags instead | [optional] [default to True]
**is_new** | **bool** | Deprecated - use productTags instead | [optional] 
**item_key** | [**ItemKey**](ItemKey.md) |  | 
**item_key_global** | [**ItemKey**](ItemKey.md) |  | [optional] 
**last_chance** | [**LastChance**](LastChance.md) |  | [optional] 
**localised_communications** | [**List[Localised]**](Localised.md) |  | [optional] 
**news** | [**News**](News.md) |  | [optional] 
**number_of_packages** | **int** |  | [optional] 
**product_name_global** | **str** |  | [optional] 
**product_tags** | [**List[ProductTag]**](ProductTag.md) |  | [optional] 
**product_type_classes** | **List[str]** | As defined by the Retail PIM Product Data Harmonizer component (based on Main Product Type) | [optional] 
**quantity** | **int** |  | 
**style_group** | **str** |  | [optional] 
**unit_code** | [**UnitCode**](UnitCode.md) |  | [optional] 

## Example

```python
from salesitem_client.models.item_child import ItemChild

# TODO update the JSON string below
json = "{}"
# create an instance of ItemChild from a JSON string
item_child_instance = ItemChild.from_json(json)
# print the JSON string representation of the object
print(ItemChild.to_json())

# convert the object into a dict
item_child_dict = item_child_instance.to_dict()
# create an instance of ItemChild from a dict
item_child_from_dict = ItemChild.from_dict(item_child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


