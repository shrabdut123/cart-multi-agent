# CouponRequest

If the user owns a coupon code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_id** | **str** |  | 

## Example

```python
from order_capture_client.models.coupon_request import CouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CouponRequest from a JSON string
coupon_request_instance = CouponRequest.from_json(json)
# print the JSON string representation of the object
print(CouponRequest.to_json())

# convert the object into a dict
coupon_request_dict = coupon_request_instance.to_dict()
# create an instance of CouponRequest from a dict
coupon_request_from_dict = CouponRequest.from_dict(coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


