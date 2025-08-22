# PriceAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of additional attribute. | [optional] 
**value** | **str** | Value of the additional attribute | [optional] 

## Example

```python
from salesitem_client.models.price_attribute import PriceAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAttribute from a JSON string
price_attribute_instance = PriceAttribute.from_json(json)
# print the JSON string representation of the object
print(PriceAttribute.to_json())

# convert the object into a dict
price_attribute_dict = price_attribute_instance.to_dict()
# create an instance of PriceAttribute from a dict
price_attribute_from_dict = PriceAttribute.from_dict(price_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


