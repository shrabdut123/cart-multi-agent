# AddOn

AddOn item completes or complements the main item by enhancing its functionality, personalization, comfort, installation, safety, care, or additional functions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_key** | [**ItemKey**](ItemKey.md) |  | [optional] 
**relation** | **str** |  | [optional] 
**main_product_type** | [**MainProductType**](MainProductType.md) |  | [optional] 
**catalogue_references** | [**List[CatalogueReference]**](CatalogueReference.md) |  | [optional] 

## Example

```python
from salesitem_client.models.add_on import AddOn

# TODO update the JSON string below
json = "{}"
# create an instance of AddOn from a JSON string
add_on_instance = AddOn.from_json(json)
# print the JSON string representation of the object
print(AddOn.to_json())

# convert the object into a dict
add_on_dict = add_on_instance.to_dict()
# create an instance of AddOn from a dict
add_on_from_dict = AddOn.from_dict(add_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


