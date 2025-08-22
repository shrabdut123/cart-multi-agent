# AccountVoucherPaymentTransaction

Account voucher transaction details

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
**payment_brand** | [**PaymentBrand**](PaymentBrand.md) |  | [optional] 
**reference** | **str** |  | [optional] 
**expiry_date** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.account_voucher_payment_transaction import AccountVoucherPaymentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of AccountVoucherPaymentTransaction from a JSON string
account_voucher_payment_transaction_instance = AccountVoucherPaymentTransaction.from_json(json)
# print the JSON string representation of the object
print(AccountVoucherPaymentTransaction.to_json())

# convert the object into a dict
account_voucher_payment_transaction_dict = account_voucher_payment_transaction_instance.to_dict()
# create an instance of AccountVoucherPaymentTransaction from a dict
account_voucher_payment_transaction_from_dict = AccountVoucherPaymentTransaction.from_dict(account_voucher_payment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


