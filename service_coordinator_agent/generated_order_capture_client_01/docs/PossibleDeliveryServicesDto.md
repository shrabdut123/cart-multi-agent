# PossibleDeliveryServicesDto

It wraps the delivery services with a metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DSRootLevelMetadataDto**](DSRootLevelMetadataDto.md) |  | [optional] 
**delivery_services** | [**List[DeliveryServiceDto]**](DeliveryServiceDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.possible_delivery_services_dto import PossibleDeliveryServicesDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleDeliveryServicesDto from a JSON string
possible_delivery_services_dto_instance = PossibleDeliveryServicesDto.from_json(json)
# print the JSON string representation of the object
print(PossibleDeliveryServicesDto.to_json())

# convert the object into a dict
possible_delivery_services_dto_dict = possible_delivery_services_dto_instance.to_dict()
# create an instance of PossibleDeliveryServicesDto from a dict
possible_delivery_services_dto_from_dict = PossibleDeliveryServicesDto.from_dict(possible_delivery_services_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


