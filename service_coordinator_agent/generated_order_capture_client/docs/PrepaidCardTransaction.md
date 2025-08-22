# PrepaidCardTransaction

Prepaid card transaction details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount for the transaction | [optional] 
**balance_amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**balance_currency** | **str** |  | [optional] 
**status** | **str** |  Transaction status of the payment , can be AUTHORIZED, CAPTURED  | [optional] 
**iopg_id** | **str** |  | [optional] 
**psp_reference_id** | **str** |  | [optional] 
**psp_timestamp** | **str** |  | [optional] 
**psp_transaction_date_time_utc** | **str** |  | [optional] 
**psp_name** | **str** |  | [optional] 
**payment_brand** | [**PaymentBrand**](PaymentBrand.md) |  | [optional] 
**payment_card_details** | [**PaymentCardDetails**](PaymentCardDetails.md) |  | [optional] 

## Example

```python
from order_capture_client.models.prepaid_card_transaction import PrepaidCardTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PrepaidCardTransaction from a JSON string
prepaid_card_transaction_instance = PrepaidCardTransaction.from_json(json)
# print the JSON string representation of the object
print(PrepaidCardTransaction.to_json())

# convert the object into a dict
prepaid_card_transaction_dict = prepaid_card_transaction_instance.to_dict()
# create an instance of PrepaidCardTransaction from a dict
prepaid_card_transaction_from_dict = PrepaidCardTransaction.from_dict(prepaid_card_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


