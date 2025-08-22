# DiscountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**value** | **float** |  | [optional] 
**max_discount_amount** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**apply_on** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.discount_details import DiscountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountDetails from a JSON string
discount_details_instance = DiscountDetails.from_json(json)
# print the JSON string representation of the object
print(DiscountDetails.to_json())

# convert the object into a dict
discount_details_dict = discount_details_instance.to_dict()
# create an instance of DiscountDetails from a dict
discount_details_from_dict = DiscountDetails.from_dict(discount_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


