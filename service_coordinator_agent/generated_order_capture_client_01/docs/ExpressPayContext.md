# ExpressPayContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**payment_context_id** | **str** |  | [optional] 
**payment_endpoint** | **str** |  | [optional] 
**checkout_id** | **str** |  | [optional] 
**redacted_address** | [**RedactedAddress**](RedactedAddress.md) |  | [optional] 
**billing_contact** | [**BillingContact**](BillingContact.md) |  | [optional] 
**shipping_contact** | [**ShippingContact**](ShippingContact.md) |  | [optional] 

## Example

```python
from order_capture_client.models.express_pay_context import ExpressPayContext

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressPayContext from a JSON string
express_pay_context_instance = ExpressPayContext.from_json(json)
# print the JSON string representation of the object
print(ExpressPayContext.to_json())

# convert the object into a dict
express_pay_context_dict = express_pay_context_instance.to_dict()
# create an instance of ExpressPayContext from a dict
express_pay_context_from_dict = ExpressPayContext.from_dict(express_pay_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


