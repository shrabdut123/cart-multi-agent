# DeliveryTimeWindowsOfTargetHDDto

It represents the target delivery timewindow details for which we need to calculate the delta prices for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slots** | [**List[DeliverySlotOfTargetHDDto]**](DeliverySlotOfTargetHDDto.md) | It represents the list of alternative slots of the target delivery with calculated delta price values | [optional] 
**earliest_possible_slot** | [**DeliverySlotOfTargetHDDto**](DeliverySlotOfTargetHDDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_time_windows_of_target_hd_dto import DeliveryTimeWindowsOfTargetHDDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryTimeWindowsOfTargetHDDto from a JSON string
delivery_time_windows_of_target_hd_dto_instance = DeliveryTimeWindowsOfTargetHDDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryTimeWindowsOfTargetHDDto.to_json())

# convert the object into a dict
delivery_time_windows_of_target_hd_dto_dict = delivery_time_windows_of_target_hd_dto_instance.to_dict()
# create an instance of DeliveryTimeWindowsOfTargetHDDto from a dict
delivery_time_windows_of_target_hd_dto_from_dict = DeliveryTimeWindowsOfTargetHDDto.from_dict(delivery_time_windows_of_target_hd_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


