# CouponMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_coupon_valid** | **bool** |  | [optional] 
**reason_of_failure** | **str** |  | [optional] 
**valid_customer_types** | **List[str]** |  | [optional] 

## Example

```python
from order_capture_client.models.coupon_metadata import CouponMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CouponMetadata from a JSON string
coupon_metadata_instance = CouponMetadata.from_json(json)
# print the JSON string representation of the object
print(CouponMetadata.to_json())

# convert the object into a dict
coupon_metadata_dict = coupon_metadata_instance.to_dict()
# create an instance of CouponMetadata from a dict
coupon_metadata_from_dict = CouponMetadata.from_dict(coupon_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


