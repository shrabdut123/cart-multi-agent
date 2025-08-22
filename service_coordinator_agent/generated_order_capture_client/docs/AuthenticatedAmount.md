# AuthenticatedAmount

Authenticated Amount for Auth&Capture details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount for the Auth &amp; Capture | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  Authenticated Amount status of the payment , can be ACCEPTED, CHALLENGED, DECLINED  | [optional] 
**payment_gateway** | **str** | Payment Transaction Payment Gateway | [optional] 
**payment_gateway_reference_id** | **str** | Reference to the customer present transaction where the customer authenticated this amount in context of paymentGateway | [optional] 
**payment_system** | **str** | Payment System which orchestrated this Customer Payment | [optional] 
**customer_payment_id** | **str** | Reference to a customer payment in context of paymentSystem, e.g. paymentContextid in case of IOPS. Could be used to group transactions in case of a multi tender payment | [optional] 
**created_date_time_utc** | **str** | Timestamp set by the PSP when this authentication was done | [optional] 
**expiry_date_time_utc** | **str** | Timestamp when this authentication expires, typically 90 days for credit card | [optional] 
**payment_brand_name** | **str** | Ingka brand for the underlying transaction | [optional] 
**last4_digits** | **str** | For convenience, details will be on the referenced transaction | [optional] 
**is_also_authorized** | **bool** | Indicates whether the amount is also authorised and not only authenticated | [optional] 

## Example

```python
from order_capture_client.models.authenticated_amount import AuthenticatedAmount

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedAmount from a JSON string
authenticated_amount_instance = AuthenticatedAmount.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedAmount.to_json())

# convert the object into a dict
authenticated_amount_dict = authenticated_amount_instance.to_dict()
# create an instance of AuthenticatedAmount from a dict
authenticated_amount_from_dict = AuthenticatedAmount.from_dict(authenticated_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


