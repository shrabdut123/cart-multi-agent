# ServiceSlotMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** |  | [optional] 
**payment_type** | **str** |  | [optional] 
**service_provider_id** | **str** |  | [optional] 
**service_provider_name** | **str** |  | [optional] 
**show_end_date** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.service_slot_metadata import ServiceSlotMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSlotMetadata from a JSON string
service_slot_metadata_instance = ServiceSlotMetadata.from_json(json)
# print the JSON string representation of the object
print(ServiceSlotMetadata.to_json())

# convert the object into a dict
service_slot_metadata_dict = service_slot_metadata_instance.to_dict()
# create an instance of ServiceSlotMetadata from a dict
service_slot_metadata_from_dict = ServiceSlotMetadata.from_dict(service_slot_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


