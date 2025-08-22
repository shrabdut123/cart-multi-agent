# OrderDiscountSummary

It represents the summary of discounts under each price type with the name of the discount. The properties available under discount summary might vary for each price type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.order_discount_summary import OrderDiscountSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDiscountSummary from a JSON string
order_discount_summary_instance = OrderDiscountSummary.from_json(json)
# print the JSON string representation of the object
print(OrderDiscountSummary.to_json())

# convert the object into a dict
order_discount_summary_dict = order_discount_summary_instance.to_dict()
# create an instance of OrderDiscountSummary from a dict
order_discount_summary_from_dict = OrderDiscountSummary.from_dict(order_discount_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


