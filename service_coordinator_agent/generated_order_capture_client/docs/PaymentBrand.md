# PaymentBrand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**psp_brand_name** | **str** |  | [optional] 
**tender_type** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**icons** | **List[str]** |  | [optional] 

## Example

```python
from order_capture_client.models.payment_brand import PaymentBrand

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBrand from a JSON string
payment_brand_instance = PaymentBrand.from_json(json)
# print the JSON string representation of the object
print(PaymentBrand.to_json())

# convert the object into a dict
payment_brand_dict = payment_brand_instance.to_dict()
# create an instance of PaymentBrand from a dict
payment_brand_from_dict = PaymentBrand.from_dict(payment_brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


