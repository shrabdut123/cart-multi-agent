# ServiceAndTimeWindowsEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_item_no** | **str** |  | [optional] 
**so_method** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**capacity_unit** | **str** |  | [optional] 
**selected_slot** | [**ServiceSlot**](ServiceSlot.md) |  | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 

## Example

```python
from order_capture_client.models.service_and_time_windows_entity import ServiceAndTimeWindowsEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceAndTimeWindowsEntity from a JSON string
service_and_time_windows_entity_instance = ServiceAndTimeWindowsEntity.from_json(json)
# print the JSON string representation of the object
print(ServiceAndTimeWindowsEntity.to_json())

# convert the object into a dict
service_and_time_windows_entity_dict = service_and_time_windows_entity_instance.to_dict()
# create an instance of ServiceAndTimeWindowsEntity from a dict
service_and_time_windows_entity_from_dict = ServiceAndTimeWindowsEntity.from_dict(service_and_time_windows_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


