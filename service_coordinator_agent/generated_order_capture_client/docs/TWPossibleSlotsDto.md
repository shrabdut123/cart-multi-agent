# TWPossibleSlotsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | [**List[DeliverySlotDto]**](DeliverySlotDto.md) | It describes the other possible slots apart from earliest slot and its additional properties. It may not be available in case of error | [optional] 
**earliest_possible_slot** | [**DeliverySlotDto**](DeliverySlotDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.tw_possible_slots_dto import TWPossibleSlotsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TWPossibleSlotsDto from a JSON string
tw_possible_slots_dto_instance = TWPossibleSlotsDto.from_json(json)
# print the JSON string representation of the object
print(TWPossibleSlotsDto.to_json())

# convert the object into a dict
tw_possible_slots_dto_dict = tw_possible_slots_dto_instance.to_dict()
# create an instance of TWPossibleSlotsDto from a dict
tw_possible_slots_dto_from_dict = TWPossibleSlotsDto.from_dict(tw_possible_slots_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


