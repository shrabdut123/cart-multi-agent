# CheckoutPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_id** | **str** | This property is not referred as it will be always referred from PATH and will beremoved shortly | [optional] 
**family_card_no** | **str** | An optional family card number, if any | [optional] 
**contact_allowed** | **bool** | This is a boolean flag to determine the active opt-in of the customer for receiving customer surveys.  | [optional] 
**profile_type** | **str** | Determines the type of user, REGULAR or BUSINESS | [optional] 
**language_code** | **str** | The language code used within the checkout initiation | [optional] 
**items** | [**List[PatchItemRequest]**](PatchItemRequest.md) |  | [optional] 
**coupons** | [**List[CouponRequest]**](CouponRequest.md) |  | [optional] 
**coupons_to_remove** | [**List[CouponRequest]**](CouponRequest.md) | It represents the coupons that user wants to remove after applying them | [optional] 

## Example

```python
from order_capture_client.models.checkout_patch_request import CheckoutPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutPatchRequest from a JSON string
checkout_patch_request_instance = CheckoutPatchRequest.from_json(json)
# print the JSON string representation of the object
print(CheckoutPatchRequest.to_json())

# convert the object into a dict
checkout_patch_request_dict = checkout_patch_request_instance.to_dict()
# create an instance of CheckoutPatchRequest from a dict
checkout_patch_request_from_dict = CheckoutPatchRequest.from_dict(checkout_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


