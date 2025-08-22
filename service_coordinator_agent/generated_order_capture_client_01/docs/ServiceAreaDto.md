# ServiceAreaDto

This is the location where the service is requested

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zip_code** | **str** | It refers to the customer service location for delivery or a service. Please note that OC will pass this zip code as-is for delivery calculation and no formatting will be applied | 
**state_code** | **str** | It refers to state code and it should be a 2 character state code. It is mandatory for US, CA, AU | [optional] 
**city** | **str** | It refers to City. This is used in Australia | [optional] 
**delivery_country_code** | **str** | This is used in case of delivery to another country in special case i.e. Luxembourg | [optional] 

## Example

```python
from order_capture_client.models.service_area_dto import ServiceAreaDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAreaDto from a JSON string
service_area_dto_instance = ServiceAreaDto.from_json(json)
# print the JSON string representation of the object
print(ServiceAreaDto.to_json())

# convert the object into a dict
service_area_dto_dict = service_area_dto_instance.to_dict()
# create an instance of ServiceAreaDto from a dict
service_area_dto_from_dict = ServiceAreaDto.from_dict(service_area_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


