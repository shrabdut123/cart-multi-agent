# ItemPrice

This node is relevant only if priceType is ITEM_PRICE. It represents the unit price details of an item. This is a discounted unit price. The properties underneath represent price with discounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incl_tax** | **float** | It represents inclTax unit price inclusive savings if a saving exist. This can be null in certain cases. In US &amp; CA, inclTax price will not be available until zip-in is completed as indicative tax calculation in complex countries requires additional information other than items and its prices | [optional] 
**excl_tax** | **float** | It represents exclTax unit price inclusive savings if a saving exist. This can be null in certain cases. Russia is an example where we will not have a tax break down until zip-in is completed | [optional] 
**tax** | **float** | It represents the tax under corresponding type. This can be null in certain cases. Example: US, CA, Russia may not have this populated in initial steps. This information is available when we progress in checkout with zip-in | [optional] 
**valid_from** | **str** | It represents the price validity. This can be null and will be removed in future | [optional] 
**valid_to** | **str** | It represents the price validity. This can be null and will be removed in future | [optional] 

## Example

```python
from order_capture_client.models.item_price import ItemPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPrice from a JSON string
item_price_instance = ItemPrice.from_json(json)
# print the JSON string representation of the object
print(ItemPrice.to_json())

# convert the object into a dict
item_price_dict = item_price_instance.to_dict()
# create an instance of ItemPrice from a dict
item_price_from_dict = ItemPrice.from_dict(item_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


