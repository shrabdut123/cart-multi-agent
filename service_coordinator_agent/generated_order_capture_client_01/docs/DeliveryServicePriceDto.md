# DeliveryServicePriceDto

It is a price for a delivery. It shall be consumed only if delivery level prices are required. In case of single delivery, this price is equivalent to solution price under DeliveryService object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incl_tax** | **float** | Not always available i.e. US &amp; CA. BigDecimal | [optional] 
**excl_tax** | **float** | Not always available i.e. for example Russia. BigDecimal | [optional] 
**original_price** | **float** | Not always available i.e. when there is no discount/coupon applied | [optional] 

## Example

```python
from order_capture_client.models.delivery_service_price_dto import DeliveryServicePriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryServicePriceDto from a JSON string
delivery_service_price_dto_instance = DeliveryServicePriceDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryServicePriceDto.to_json())

# convert the object into a dict
delivery_service_price_dto_dict = delivery_service_price_dto_instance.to_dict()
# create an instance of DeliveryServicePriceDto from a dict
delivery_service_price_dto_from_dict = DeliveryServicePriceDto.from_dict(delivery_service_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


