# ProductTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**valid_from** | **date** |  | [optional] 
**valid_to** | **date** |  | [optional] 

## Example

```python
from salesitem_client.models.product_tag import ProductTag

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTag from a JSON string
product_tag_instance = ProductTag.from_json(json)
# print the JSON string representation of the object
print(ProductTag.to_json())

# convert the object into a dict
product_tag_dict = product_tag_instance.to_dict()
# create an instance of ProductTag from a dict
product_tag_from_dict = ProductTag.from_dict(product_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


