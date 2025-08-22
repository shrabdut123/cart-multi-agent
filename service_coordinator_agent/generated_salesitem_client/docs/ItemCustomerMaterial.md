# ItemCustomerMaterial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_materials** | [**List[ItemPartMaterial]**](ItemPartMaterial.md) |  | [optional] 
**product_type_text** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_customer_material import ItemCustomerMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCustomerMaterial from a JSON string
item_customer_material_instance = ItemCustomerMaterial.from_json(json)
# print the JSON string representation of the object
print(ItemCustomerMaterial.to_json())

# convert the object into a dict
item_customer_material_dict = item_customer_material_instance.to_dict()
# create an instance of ItemCustomerMaterial from a dict
item_customer_material_from_dict = ItemCustomerMaterial.from_dict(item_customer_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


