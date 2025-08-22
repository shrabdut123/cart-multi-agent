# PUPPrice

It is for future use

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incl_tax** | **float** | Not always available i.e. US &amp; CA. BigDecimal | [optional] 
**excl_tax** | **float** | Not always available i.e. for example Russia. BigDecimal | [optional] 
**original_price** | **float** |  | [optional] 

## Example

```python
from order_capture_client.models.pup_price import PUPPrice

# TODO update the JSON string below
json = "{}"
# create an instance of PUPPrice from a JSON string
pup_price_instance = PUPPrice.from_json(json)
# print the JSON string representation of the object
print(PUPPrice.to_json())

# convert the object into a dict
pup_price_dict = pup_price_instance.to_dict()
# create an instance of PUPPrice from a dict
pup_price_from_dict = PUPPrice.from_dict(pup_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


