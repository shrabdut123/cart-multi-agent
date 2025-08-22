# ServiceAreaRequest

Determines the details of delivery area. e.g zipCode, stateCode, and city

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zip_code** | **str** |  | 
**state_code** | **str** | Mandatory for US | [optional] 
**city** | **str** |  | [optional] 
**delivery_country_code** | **str** | This is used in case of delivery to another country in special case i.e. Luxembourg | [optional] 

## Example

```python
from order_capture_client.models.service_area_request import ServiceAreaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAreaRequest from a JSON string
service_area_request_instance = ServiceAreaRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceAreaRequest.to_json())

# convert the object into a dict
service_area_request_dict = service_area_request_instance.to_dict()
# create an instance of ServiceAreaRequest from a dict
service_area_request_from_dict = ServiceAreaRequest.from_dict(service_area_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


