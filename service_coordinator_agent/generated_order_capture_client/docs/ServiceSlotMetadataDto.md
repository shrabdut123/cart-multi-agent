# ServiceSlotMetadataDto

It describes the slot metadata such as timezone, payment info, service provider name etc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | It describes the time zone | [optional] 
**payment_type** | **str** | It is a service offer provided value that describes whether a payment is done to IKEA or to Service provider directly | [optional] 
**service_provider_id** | **str** | It is a service offer provided value that identifies the service provider | [optional] 
**service_provider_name** | **str** | It is a service offer provided value that identifies the service provider | [optional] 
**show_end_date** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.service_slot_metadata_dto import ServiceSlotMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSlotMetadataDto from a JSON string
service_slot_metadata_dto_instance = ServiceSlotMetadataDto.from_json(json)
# print the JSON string representation of the object
print(ServiceSlotMetadataDto.to_json())

# convert the object into a dict
service_slot_metadata_dto_dict = service_slot_metadata_dto_instance.to_dict()
# create an instance of ServiceSlotMetadataDto from a dict
service_slot_metadata_dto_from_dict = ServiceSlotMetadataDto.from_dict(service_slot_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


