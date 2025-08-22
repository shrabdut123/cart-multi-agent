# PayOnDelivery

Pay on delivery transaction details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount for the transaction | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.pay_on_delivery import PayOnDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of PayOnDelivery from a JSON string
pay_on_delivery_instance = PayOnDelivery.from_json(json)
# print the JSON string representation of the object
print(PayOnDelivery.to_json())

# convert the object into a dict
pay_on_delivery_dict = pay_on_delivery_instance.to_dict()
# create an instance of PayOnDelivery from a dict
pay_on_delivery_from_dict = PayOnDelivery.from_dict(pay_on_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


