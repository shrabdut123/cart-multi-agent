# CreditCardTransaction

Status of Payment can be COMPLETED or DELAYED RESULT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount for the transaction | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  Transaction status of the payment , can be AUTHORIZED, CAPTURED  | [optional] 
**iopg_id** | **str** |  | [optional] 
**psp_reference_id** | **str** |  | [optional] 
**psp_timestamp** | **str** |  | [optional] 
**psp_transaction_date_time_utc** | **str** |  | [optional] 
**psp_name** | **str** |  | [optional] 
**authorisation_code** | **str** |  | [optional] 
**payment_brand** | [**PaymentBrand**](PaymentBrand.md) |  | [optional] 
**payment_card_details** | [**PaymentCardDetails**](PaymentCardDetails.md) |  | [optional] 
**decline_reason** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.credit_card_transaction import CreditCardTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardTransaction from a JSON string
credit_card_transaction_instance = CreditCardTransaction.from_json(json)
# print the JSON string representation of the object
print(CreditCardTransaction.to_json())

# convert the object into a dict
credit_card_transaction_dict = credit_card_transaction_instance.to_dict()
# create an instance of CreditCardTransaction from a dict
credit_card_transaction_from_dict = CreditCardTransaction.from_dict(credit_card_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


