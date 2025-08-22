# SpeCoupon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_code** | **str** |  | [optional] 
**discount_amount** | [**List[SpeAmount]**](SpeAmount.md) |  | [optional] 
**info_messages** | [**List[SpeInfoMessage]**](SpeInfoMessage.md) |  | [optional] 
**texts** | [**List[SpeCouponText]**](SpeCouponText.md) |  | [optional] 
**valid_customer_types** | **List[str]** |  | [optional] 
**service_discount** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.spe_coupon import SpeCoupon

# TODO update the JSON string below
json = "{}"
# create an instance of SpeCoupon from a JSON string
spe_coupon_instance = SpeCoupon.from_json(json)
# print the JSON string representation of the object
print(SpeCoupon.to_json())

# convert the object into a dict
spe_coupon_dict = spe_coupon_instance.to_dict()
# create an instance of SpeCoupon from a dict
spe_coupon_from_dict = SpeCoupon.from_dict(spe_coupon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


