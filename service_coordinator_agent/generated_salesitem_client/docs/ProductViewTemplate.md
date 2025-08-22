# ProductViewTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.product_view_template import ProductViewTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProductViewTemplate from a JSON string
product_view_template_instance = ProductViewTemplate.from_json(json)
# print the JSON string representation of the object
print(ProductViewTemplate.to_json())

# convert the object into a dict
product_view_template_dict = product_view_template_instance.to_dict()
# create an instance of ProductViewTemplate from a dict
product_view_template_from_dict = ProductViewTemplate.from_dict(product_view_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


