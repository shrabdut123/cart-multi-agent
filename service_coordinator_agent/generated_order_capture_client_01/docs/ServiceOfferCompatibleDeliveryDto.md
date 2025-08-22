# ServiceOfferCompatibleDeliveryDto

It describes if the delivery service is compatible with service offer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_service_item_no** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.service_offer_compatible_delivery_dto import ServiceOfferCompatibleDeliveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceOfferCompatibleDeliveryDto from a JSON string
service_offer_compatible_delivery_dto_instance = ServiceOfferCompatibleDeliveryDto.from_json(json)
# print the JSON string representation of the object
print(ServiceOfferCompatibleDeliveryDto.to_json())

# convert the object into a dict
service_offer_compatible_delivery_dto_dict = service_offer_compatible_delivery_dto_instance.to_dict()
# create an instance of ServiceOfferCompatibleDeliveryDto from a dict
service_offer_compatible_delivery_dto_from_dict = ServiceOfferCompatibleDeliveryDto.from_dict(service_offer_compatible_delivery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


