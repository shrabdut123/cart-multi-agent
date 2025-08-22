# DSConfigDto

The delivery service configuration that describes properties such as prime time, lead time orchestration etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_lead_time_orchestration** | **bool** | It describes if lead time orchestration is enabled and used | [optional] 
**enable_prime_time_calculation** | **bool** | It describes if prime time slot is enabled for a retail unit | [optional] 
**service_offer_compatible_deliveries** | [**List[ServiceOfferCompatibleDeliveryDto]**](ServiceOfferCompatibleDeliveryDto.md) | It describes if the delivery service is compatible with service offer | [optional] 
**allowed_pts_deliveries** | **List[str]** | It has a list of delivery services supported i.e. HOME_DELIVERY_STANDARD, HOME_DELIVERY_CURBSIDE | [optional] 

## Example

```python
from order_capture_client.models.ds_config_dto import DSConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of DSConfigDto from a JSON string
ds_config_dto_instance = DSConfigDto.from_json(json)
# print the JSON string representation of the object
print(DSConfigDto.to_json())

# convert the object into a dict
ds_config_dto_dict = ds_config_dto_instance.to_dict()
# create an instance of DSConfigDto from a dict
ds_config_dto_from_dict = DSConfigDto.from_dict(ds_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


