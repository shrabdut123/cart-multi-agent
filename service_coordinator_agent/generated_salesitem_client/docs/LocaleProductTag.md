# LocaleProductTag

Defines locale-specific tags that can be associated with an item. For example, a tag of type `SLEEP_ON_IT_DAYS` with values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**values** | [**List[LocaleProductTagValue]**](LocaleProductTagValue.md) |  | [optional] 

## Example

```python
from salesitem_client.models.locale_product_tag import LocaleProductTag

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleProductTag from a JSON string
locale_product_tag_instance = LocaleProductTag.from_json(json)
# print the JSON string representation of the object
print(LocaleProductTag.to_json())

# convert the object into a dict
locale_product_tag_dict = locale_product_tag_instance.to_dict()
# create an instance of LocaleProductTag from a dict
locale_product_tag_from_dict = LocaleProductTag.from_dict(locale_product_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


