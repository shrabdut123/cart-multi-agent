# ExpressPayContextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**payment_context_id** | **str** |  | [optional] 
**payment_endpoint** | **str** |  | [optional] 
**checkout_id** | **str** |  | [optional] 
**redacted_address** | [**RedactedAddressRequest**](RedactedAddressRequest.md) |  | [optional] 
**billing_contact** | [**BillingContactRequest**](BillingContactRequest.md) |  | [optional] 
**shipping_contact** | [**ShippingContactRequest**](ShippingContactRequest.md) |  | [optional] 

## Example

```python
from order_capture_client.models.express_pay_context_request import ExpressPayContextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressPayContextRequest from a JSON string
express_pay_context_request_instance = ExpressPayContextRequest.from_json(json)
# print the JSON string representation of the object
print(ExpressPayContextRequest.to_json())

# convert the object into a dict
express_pay_context_request_dict = express_pay_context_request_instance.to_dict()
# create an instance of ExpressPayContextRequest from a dict
express_pay_context_request_from_dict = ExpressPayContextRequest.from_dict(express_pay_context_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


