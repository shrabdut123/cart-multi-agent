# BusinessCreditTransaction

Business card transaction details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount for the transaction | [optional] 
**purchase_order_number** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  Transaction status of the payment , can be AUTHORIZED, CAPTURED  | [optional] 
**iopg_id** | **str** |  | [optional] 
**psp_reference_id** | **str** |  | [optional] 
**authorisation_code** | **str** |  | [optional] 
**psp_timestamp** | **str** |  | [optional] 
**psp_transaction_date_time_utc** | **str** |  | [optional] 
**psp_name** | **str** |  | [optional] 
**payment_brand** | [**PaymentBrand**](PaymentBrand.md) |  | [optional] 
**payment_card_details** | [**PaymentCardDetails**](PaymentCardDetails.md) |  | [optional] 
**decline_reason** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**account_number_source** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.business_credit_transaction import BusinessCreditTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessCreditTransaction from a JSON string
business_credit_transaction_instance = BusinessCreditTransaction.from_json(json)
# print the JSON string representation of the object
print(BusinessCreditTransaction.to_json())

# convert the object into a dict
business_credit_transaction_dict = business_credit_transaction_instance.to_dict()
# create an instance of BusinessCreditTransaction from a dict
business_credit_transaction_from_dict = BusinessCreditTransaction.from_dict(business_credit_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


