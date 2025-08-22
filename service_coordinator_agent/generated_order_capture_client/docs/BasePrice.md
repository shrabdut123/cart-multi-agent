# BasePrice

It represents the main price structure from family customer point of view. The presence of node does not guarantee that a family price exist. This must be used only for up-sell purpose and should. If not for up-sell, the properties under price must be consumed directly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incl_tax** | **float** | It represents inclTax price inclusive savings if a saving exist. This can be null in certain cases. In US &amp; CA, inclTax price will not be available until zip-in is completed as indicative tax calculation in complex countries requires additional information other than items and its prices | [optional] 
**excl_tax** | **float** | It represents exclTax price inclusive savings if a saving exist. This can be null in certain cases. Russia is an example where we will not have a tax break down until zip-in is completed | [optional] 
**tax** | **float** | It represents the tax under corresponding type. This can be null in certain cases. Example: US, CA, Russia may not have this populated in initial steps. This information is available when we progress in checkout with zip-in | [optional] 
**tax_list** | [**List[Tax]**](Tax.md) | It represents the breakdown of taxes. This can be null in certain cases. Example: US, CA, Russia may not have this populated in initial steps. This information is available when we progress in checkout with zip-in | [optional] 
**discount_list** | [**List[Discount]**](Discount.md) | It represents the details of the discounts that are applied under a corresponding type of price. This provides a detailed view of discounts and client usage is not recommended. This node will be removed in future. | [optional] 
**discount_summary** | [**DiscountSummary**](DiscountSummary.md) |  | [optional] 
**order_discount_summary_list** | [**List[OrderDiscountSummary]**](OrderDiscountSummary.md) | It represents the summary of discounts under each price type with the name of the discount. The properties available under discount summary might vary for each price type | [optional] 
**per_item_price** | [**ItemPrice**](ItemPrice.md) |  | [optional] 
**per_item_sale_price** | [**ItemPrice**](ItemPrice.md) |  | [optional] 
**tax_summary_list** | [**List[SpeTaxSummary]**](SpeTaxSummary.md) | It represents the tax summary list. This can be null under item lines. It is relevant to consume this property only under the price type ORDER_TOTAL | [optional] 
**price_excl_savings** | [**PriceExclSavings**](PriceExclSavings.md) |  | [optional] 
**total_order_savings** | **float** |  | [optional] 

## Example

```python
from order_capture_client.models.base_price import BasePrice

# TODO update the JSON string below
json = "{}"
# create an instance of BasePrice from a JSON string
base_price_instance = BasePrice.from_json(json)
# print the JSON string representation of the object
print(BasePrice.to_json())

# convert the object into a dict
base_price_dict = base_price_instance.to_dict()
# create an instance of BasePrice from a dict
base_price_from_dict = BasePrice.from_dict(base_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


