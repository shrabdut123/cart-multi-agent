# PaymentContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**payment_context_id** | **str** |  | [optional] 
**payment_endpoint** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.payment_context import PaymentContext

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentContext from a JSON string
payment_context_instance = PaymentContext.from_json(json)
# print the JSON string representation of the object
print(PaymentContext.to_json())

# convert the object into a dict
payment_context_dict = payment_context_instance.to_dict()
# create an instance of PaymentContext from a dict
payment_context_from_dict = PaymentContext.from_dict(payment_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


