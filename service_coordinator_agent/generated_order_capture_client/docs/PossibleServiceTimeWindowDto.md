# PossibleServiceTimeWindowDto

It describes the time windows for each service that was added in cart and active i.e. supported by the service and other parameters such as co-worker assistance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_item_no** | **str** | It describes the unique identifier of a service | [optional] 
**so_method** | **str** | It is a type of service. At present, PROVIDED are supported. It is provided by Service offer | [optional] 
**service_id** | **str** | It describes the service. It is provided by Service offer | [optional] 
**service_type** | **str** | It is a type of service. It is provided by Service offer | [optional] 
**capacity_unit** | **str** | Service offer provided value. Usually it is not presented to customer. | [optional] 
**earliest_possible_slot** | [**ServiceSlotDto**](ServiceSlotDto.md) |  | [optional] 
**slots** | [**List[ServiceSlotDto]**](ServiceSlotDto.md) | It is same as above but it contains the list of alternate start slots that can be used for calendar presentation | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from order_capture_client.models.possible_service_time_window_dto import PossibleServiceTimeWindowDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleServiceTimeWindowDto from a JSON string
possible_service_time_window_dto_instance = PossibleServiceTimeWindowDto.from_json(json)
# print the JSON string representation of the object
print(PossibleServiceTimeWindowDto.to_json())

# convert the object into a dict
possible_service_time_window_dto_dict = possible_service_time_window_dto_instance.to_dict()
# create an instance of PossibleServiceTimeWindowDto from a dict
possible_service_time_window_dto_from_dict = PossibleServiceTimeWindowDto.from_dict(possible_service_time_window_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


