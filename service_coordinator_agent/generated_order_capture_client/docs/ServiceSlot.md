# ServiceSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ServiceSlotMetadata**](ServiceSlotMetadata.md) |  | [optional] 
**id** | **str** |  | [optional] 
**from_date_time** | **str** |  | [optional] 
**to_date_time** | **str** |  | [optional] 
**from_date_time_utc** | **str** |  | [optional] 
**to_date_time_utc** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**capacity_allocated** | **str** |  | [optional] 
**span_slots** | [**List[ServiceSpanSlot]**](ServiceSpanSlot.md) |  | [optional] 

## Example

```python
from order_capture_client.models.service_slot import ServiceSlot

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSlot from a JSON string
service_slot_instance = ServiceSlot.from_json(json)
# print the JSON string representation of the object
print(ServiceSlot.to_json())

# convert the object into a dict
service_slot_dict = service_slot_instance.to_dict()
# create an instance of ServiceSlot from a dict
service_slot_from_dict = ServiceSlot.from_dict(service_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


