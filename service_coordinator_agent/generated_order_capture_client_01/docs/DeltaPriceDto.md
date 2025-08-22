# DeltaPriceDto

It is for future use

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incl_tax** | **float** | Not always available i.e. US &amp; CA. BigDecimal | [optional] 
**excl_tax** | **float** | Not always available i.e. for example Russia. BigDecimal | [optional] 
**delta_price** | **float** | It represents the value of deliveryService for the PUP after deducting the price of previous selected PUP in case of split delivery | [optional] 

## Example

```python
from order_capture_client.models.delta_price_dto import DeltaPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaPriceDto from a JSON string
delta_price_dto_instance = DeltaPriceDto.from_json(json)
# print the JSON string representation of the object
print(DeltaPriceDto.to_json())

# convert the object into a dict
delta_price_dto_dict = delta_price_dto_instance.to_dict()
# create an instance of DeltaPriceDto from a dict
delta_price_dto_from_dict = DeltaPriceDto.from_dict(delta_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


