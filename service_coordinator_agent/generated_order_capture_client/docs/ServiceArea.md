# ServiceArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zip_code** | **str** | It refers to the customer service location for delivery or a service. Please note that OC will pass this zip code as-is for delivery calculation and no formatting will be applied | [optional] 
**state_code** | **str** | It refers to state code and it should be a 2 character state code. It is mandatory for US, CA, AU | [optional] 
**city** | **str** | It refers to state code and it should be a 2 character state code. It is mandatory for US, CA, AU | [optional] 
**id** | **str** | OC generated UUID for the service area | [optional] 
**delivery_country_code** | **str** | This is used in case of delivery to another country in special case i.e. Luxembourg | [optional] 

## Example

```python
from order_capture_client.models.service_area import ServiceArea

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceArea from a JSON string
service_area_instance = ServiceArea.from_json(json)
# print the JSON string representation of the object
print(ServiceArea.to_json())

# convert the object into a dict
service_area_dict = service_area_instance.to_dict()
# create an instance of ServiceArea from a dict
service_area_from_dict = ServiceArea.from_dict(service_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


