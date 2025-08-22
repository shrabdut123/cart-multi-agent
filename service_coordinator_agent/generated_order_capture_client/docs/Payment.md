# Payment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**payment_context_id** | **str** | Payment Context ID from IOPG | [optional] 
**status** | **str** | Status of Payment can be COMPLETED or DELAYED RESULT | [optional] 
**amount_left_to_pay** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**order_hash** | **str** |  | [optional] 
**credit_card_transactions** | [**List[CreditCardTransaction]**](CreditCardTransaction.md) | Status of Payment can be COMPLETED or DELAYED RESULT | [optional] 
**prepaid_card_transactions** | [**List[PrepaidCardTransaction]**](PrepaidCardTransaction.md) | Prepaid card transaction details | [optional] 
**business_credit_transactions** | [**List[BusinessCreditTransaction]**](BusinessCreditTransaction.md) | Business card transaction details | [optional] 
**open_invoice_transactions** | [**List[OpenInvoiceTransaction]**](OpenInvoiceTransaction.md) | Open invoice transaction details | [optional] 
**wallet_transactions** | [**List[WalletTransaction]**](WalletTransaction.md) | Wallet transaction details | [optional] 
**online_transfer_transactions** | [**List[OnlineTransferTransaction]**](OnlineTransferTransaction.md) | Online card transaction details | [optional] 
**account_voucher_payment_transactions** | [**List[AccountVoucherPaymentTransaction]**](AccountVoucherPaymentTransaction.md) | Account voucher transaction details | [optional] 
**credit_application_transactions** | [**List[CreditApplicationTransaction]**](CreditApplicationTransaction.md) | Credit Application transaction details | [optional] 
**authenticated_amounts** | [**List[AuthenticatedAmount]**](AuthenticatedAmount.md) | Authenticated Amount for Auth&amp;Capture details | [optional] 
**pay_on_delivery** | [**PayOnDelivery**](PayOnDelivery.md) |  | [optional] 
**pay_on_collect** | [**PayOnCollect**](PayOnCollect.md) |  | [optional] 

## Example

```python
from order_capture_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


