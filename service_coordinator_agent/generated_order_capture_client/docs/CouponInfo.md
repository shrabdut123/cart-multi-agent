# CouponInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_code** | **str** |  | [optional] 
**discount_amount** | **float** |  | [optional] 
**roll_up_price_type** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**coupon_metadata** | [**CouponMetadata**](CouponMetadata.md) |  | [optional] 

## Example

```python
from order_capture_client.models.coupon_info import CouponInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CouponInfo from a JSON string
coupon_info_instance = CouponInfo.from_json(json)
# print the JSON string representation of the object
print(CouponInfo.to_json())

# convert the object into a dict
coupon_info_dict = coupon_info_instance.to_dict()
# create an instance of CouponInfo from a dict
coupon_info_from_dict = CouponInfo.from_dict(coupon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


