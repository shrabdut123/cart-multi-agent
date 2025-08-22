# ItemCommunication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_ons** | [**List[AddOn]**](AddOn.md) |  | [optional] 
**business_structure** | [**BusinessStructure**](BusinessStructure.md) |  | [optional] 
**catalogue_references** | [**List[CatalogueReference]**](CatalogueReference.md) |  | [optional] 
**child_items** | [**List[ItemChild]**](ItemChild.md) |  | [optional] 
**class_unit_key** | [**ClassUnitKey**](ClassUnitKey.md) |  | [optional] 
**complementary_items** | [**List[ComplementaryItem]**](ComplementaryItem.md) |  | [optional] 
**filter_classes** | **List[str]** |  | [optional] 
**generic_product** | [**GenericProduct**](GenericProduct.md) |  | [optional] 
**is_assembly_required** | **bool** |  | [optional] 
**is_breath_taking_item** | **bool** | Deprecated - use productTags instead | [optional] [default to True]
**is_new** | **bool** | Deprecated - use productTags instead | [optional] 
**item_key** | [**ItemKey**](ItemKey.md) |  | [optional] 
**item_key_global** | [**ItemKey**](ItemKey.md) |  | [optional] 
**kitchen_unit** | [**KitchenUnit**](KitchenUnit.md) |  | [optional] 
**last_chance** | [**LastChance**](LastChance.md) |  | [optional] 
**localised_communications** | [**List[Localised]**](Localised.md) |  | [optional] 
**news** | [**News**](News.md) |  | [optional] 
**number_of_packages** | **int** |  | [optional] 
**presentation_group_code** | **str** |  | [optional] 
**price_quality_classification** | [**PriceQualityClassification**](PriceQualityClassification.md) |  | [optional] 
**product_name_global** | **str** |  | [optional] 
**product_tags** | [**List[ProductTag]**](ProductTag.md) |  | [optional] 
**product_type_classes** | **List[str]** | As defined by the Retail PIM Product Data Harmonizer component (based on Main Product Type) | [optional] 
**product_view_template** | [**ProductViewTemplate**](ProductViewTemplate.md) |  | [optional] 
**professional_assembly_time** | [**ProfessionalAssemblyTime**](ProfessionalAssemblyTime.md) |  | [optional] 
**service_product_relations** | [**List[ServiceProductRelation]**](ServiceProductRelation.md) |  | [optional] 
**style_group** | **str** |  | [optional] 
**unit_code** | [**UnitCode**](UnitCode.md) |  | [optional] 
**experimental** | [**List[ExperimentalItem]**](ExperimentalItem.md) | Experimental features used for testing which can be removed at any time. | [optional] 
**update_date_time** | **datetime** |  | [optional] 

## Example

```python
from salesitem_client.models.item_communication import ItemCommunication

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCommunication from a JSON string
item_communication_instance = ItemCommunication.from_json(json)
# print the JSON string representation of the object
print(ItemCommunication.to_json())

# convert the object into a dict
item_communication_dict = item_communication_instance.to_dict()
# create an instance of ItemCommunication from a dict
item_communication_from_dict = ItemCommunication.from_dict(item_communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


