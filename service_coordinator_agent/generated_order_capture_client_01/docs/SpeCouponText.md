# SpeCouponText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.spe_coupon_text import SpeCouponText

# TODO update the JSON string below
json = "{}"
# create an instance of SpeCouponText from a JSON string
spe_coupon_text_instance = SpeCouponText.from_json(json)
# print the JSON string representation of the object
print(SpeCouponText.to_json())

# convert the object into a dict
spe_coupon_text_dict = spe_coupon_text_instance.to_dict()
# create an instance of SpeCouponText from a dict
spe_coupon_text_from_dict = SpeCouponText.from_dict(spe_coupon_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


