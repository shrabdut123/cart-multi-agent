# PaymentCardDetails

Payment card details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin** | **str** |  | [optional] 
**last4_digits** | **str** |  | [optional] 
**expiry_month** | **str** |  | [optional] 
**expiry_year** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.payment_card_details import PaymentCardDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCardDetails from a JSON string
payment_card_details_instance = PaymentCardDetails.from_json(json)
# print the JSON string representation of the object
print(PaymentCardDetails.to_json())

# convert the object into a dict
payment_card_details_dict = payment_card_details_instance.to_dict()
# create an instance of PaymentCardDetails from a dict
payment_card_details_from_dict = PaymentCardDetails.from_dict(payment_card_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


