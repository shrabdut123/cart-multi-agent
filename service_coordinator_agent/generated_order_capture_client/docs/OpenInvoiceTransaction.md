# OpenInvoiceTransaction

Open invoice transaction details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**iopg_id** | **str** |  | [optional] 
**psp_reference_id** | **str** |  | [optional] 
**psp_timestamp** | **str** |  | [optional] 
**psp_transaction_date_time_utc** | **str** |  | [optional] 
**psp_name** | **str** |  | [optional] 
**payment_brand** | [**PaymentBrand**](PaymentBrand.md) |  | [optional] 
**decline_reason** | **str** |  | [optional] 
**authorization_expiry_date** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.open_invoice_transaction import OpenInvoiceTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of OpenInvoiceTransaction from a JSON string
open_invoice_transaction_instance = OpenInvoiceTransaction.from_json(json)
# print the JSON string representation of the object
print(OpenInvoiceTransaction.to_json())

# convert the object into a dict
open_invoice_transaction_dict = open_invoice_transaction_instance.to_dict()
# create an instance of OpenInvoiceTransaction from a dict
open_invoice_transaction_from_dict = OpenInvoiceTransaction.from_dict(open_invoice_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


