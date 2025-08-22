# ItemPartMaterial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**material_text** | **str** |  | [optional] 
**part_text** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_part_material import ItemPartMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPartMaterial from a JSON string
item_part_material_instance = ItemPartMaterial.from_json(json)
# print the JSON string representation of the object
print(ItemPartMaterial.to_json())

# convert the object into a dict
item_part_material_dict = item_part_material_instance.to_dict()
# create an instance of ItemPartMaterial from a dict
item_part_material_from_dict = ItemPartMaterial.from_dict(item_part_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


