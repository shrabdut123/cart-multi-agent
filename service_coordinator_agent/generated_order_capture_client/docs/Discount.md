# Discount

It represents the details of the discounts that are applied under a corresponding type of price. This provides a detailed view of discounts and client usage is not recommended. This node will be removed in future.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**discount_details** | [**DiscountDetails**](DiscountDetails.md) |  | [optional] 
**id** | **str** |  | [optional] 
**sequence** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**discount_type** | **str** |  | [optional] 
**discount_level** | **str** |  | [optional] 
**valid_from_date** | **str** |  | [optional] 
**valid_to_date** | **str** |  | [optional] 
**applied** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.discount import Discount

# TODO update the JSON string below
json = "{}"
# create an instance of Discount from a JSON string
discount_instance = Discount.from_json(json)
# print the JSON string representation of the object
print(Discount.to_json())

# convert the object into a dict
discount_dict = discount_instance.to_dict()
# create an instance of Discount from a dict
discount_from_dict = Discount.from_dict(discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


