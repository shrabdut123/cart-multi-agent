# ServiceSpanSlotDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**from_date_time** | **str** |  | [optional] 
**to_date_time** | **str** |  | [optional] 
**capacity_allocated** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.service_span_slot_dto import ServiceSpanSlotDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSpanSlotDto from a JSON string
service_span_slot_dto_instance = ServiceSpanSlotDto.from_json(json)
# print the JSON string representation of the object
print(ServiceSpanSlotDto.to_json())

# convert the object into a dict
service_span_slot_dto_dict = service_span_slot_dto_instance.to_dict()
# create an instance of ServiceSpanSlotDto from a dict
service_span_slot_dto_from_dict = ServiceSpanSlotDto.from_dict(service_span_slot_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


