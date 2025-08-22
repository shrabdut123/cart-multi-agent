# OnlineTransferTransaction

Online card transaction details

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

## Example

```python
from order_capture_client.models.online_transfer_transaction import OnlineTransferTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of OnlineTransferTransaction from a JSON string
online_transfer_transaction_instance = OnlineTransferTransaction.from_json(json)
# print the JSON string representation of the object
print(OnlineTransferTransaction.to_json())

# convert the object into a dict
online_transfer_transaction_dict = online_transfer_transaction_instance.to_dict()
# create an instance of OnlineTransferTransaction from a dict
online_transfer_transaction_from_dict = OnlineTransferTransaction.from_dict(online_transfer_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


