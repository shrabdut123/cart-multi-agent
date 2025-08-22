# ServiceItemDto

This contains the list of services requested along with its details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_item_no** | **str** | It identifies a service item. Usually a string starting with SGR for IKEA, TASKRABBIT for TASKRABBIT provider | [optional] 
**service_product_id** | **str** | It identifies a service product | [optional] 
**item_references** | [**List[ItemReferenceDto]**](ItemReferenceDto.md) | It refers to the items for which the service is requested | [optional] 
**provider** | **str** | It identifies the type of provider i.e. IKEA or TASKRABBIT for example | [optional] 

## Example

```python
from order_capture_client.models.service_item_dto import ServiceItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceItemDto from a JSON string
service_item_dto_instance = ServiceItemDto.from_json(json)
# print the JSON string representation of the object
print(ServiceItemDto.to_json())

# convert the object into a dict
service_item_dto_dict = service_item_dto_instance.to_dict()
# create an instance of ServiceItemDto from a dict
service_item_dto_from_dict = ServiceItemDto.from_dict(service_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


