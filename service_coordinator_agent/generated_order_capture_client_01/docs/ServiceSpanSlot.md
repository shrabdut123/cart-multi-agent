# ServiceSpanSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**from_date_time** | **str** |  | [optional] 
**to_date_time** | **str** |  | [optional] 
**from_date_time_utc** | **str** |  | [optional] 
**to_date_time_utc** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**capacity_allocated** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.service_span_slot import ServiceSpanSlot

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSpanSlot from a JSON string
service_span_slot_instance = ServiceSpanSlot.from_json(json)
# print the JSON string representation of the object
print(ServiceSpanSlot.to_json())

# convert the object into a dict
service_span_slot_dict = service_span_slot_instance.to_dict()
# create an instance of ServiceSpanSlot from a dict
service_span_slot_from_dict = ServiceSpanSlot.from_dict(service_span_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


