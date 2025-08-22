# DiscountSummary

It represents the summary of discounts under each price type. The properties available under discount summary might vary for each price type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **float** | It represents the sum of all savings including familyPrice. Not relevant if the priceType is ORDER_TOTAL | [optional] 
**discounts** | **float** | It represents the sum of all SDM savings. Only relevant if the priceType is ORDER_TOTAL | [optional] 
**family_price** | **float** | It represents the total savings of familyPrice associated with items. This must not be confused with SDM family savings | [optional] 
**promotions** | **float** | This is copy of discounts. It will be removed in future | [optional] 
**coupons** | **float** | It represents the savings connected to a coupon. Only relevant if the priceType is ORDER_TOTAL | [optional] 
**employee** | **float** | It represents the savings connected to an employee discount. Only relevant if the priceType is ORDER_TOTAL | [optional] 
**family_promotions** | **float** | It represents the copy of familyDiscounts. It is deprecated and will be removed in future | [optional] 
**family_discounts** | **float** | It represents the savings connected to SDM family discounts. This is possible even if there are no family items in cart. Only relevant if the priceType is ORDER_TOTAL | [optional] 
**family** | **float** | It represents a sum of familyPrice and familyDiscount savings. Only relevant if the priceType is ORDER_TOTAL | [optional] 
**manual** | **float** | It is not relevant for web. It will be removed in future | [optional] 
**voucher** | **float** | It represents the savings connected to a voucher. Only relevant if the priceType is ORDER_TOTAL | [optional] 

## Example

```python
from order_capture_client.models.discount_summary import DiscountSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountSummary from a JSON string
discount_summary_instance = DiscountSummary.from_json(json)
# print the JSON string representation of the object
print(DiscountSummary.to_json())

# convert the object into a dict
discount_summary_dict = discount_summary_instance.to_dict()
# create an instance of DiscountSummary from a dict
discount_summary_from_dict = DiscountSummary.from_dict(discount_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


