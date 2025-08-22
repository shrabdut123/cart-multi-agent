# LocaleProductTagValue

The value can be a URL or a number, depending on the type. For RETURN_POLICY_URL, it will be a URL. For NUMBER_OF_DAYS, it will be a number in string format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from salesitem_client.models.locale_product_tag_value import LocaleProductTagValue

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleProductTagValue from a JSON string
locale_product_tag_value_instance = LocaleProductTagValue.from_json(json)
# print the JSON string representation of the object
print(LocaleProductTagValue.to_json())

# convert the object into a dict
locale_product_tag_value_dict = locale_product_tag_value_instance.to_dict()
# create an instance of LocaleProductTagValue from a dict
locale_product_tag_value_from_dict = LocaleProductTagValue.from_dict(locale_product_tag_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


