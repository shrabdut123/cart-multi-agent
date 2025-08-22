# DeltaPriceTimeSlotResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_home_delivery_service** | [**SelectedHomeDeliveryServiceDto**](SelectedHomeDeliveryServiceDto.md) |  | [optional] 
**delta_prices_of_the_target_hd** | [**DeltaPriceOfTheTargetHDDto**](DeltaPriceOfTheTargetHDDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delta_price_time_slot_response_dto import DeltaPriceTimeSlotResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaPriceTimeSlotResponseDto from a JSON string
delta_price_time_slot_response_dto_instance = DeltaPriceTimeSlotResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeltaPriceTimeSlotResponseDto.to_json())

# convert the object into a dict
delta_price_time_slot_response_dto_dict = delta_price_time_slot_response_dto_instance.to_dict()
# create an instance of DeltaPriceTimeSlotResponseDto from a dict
delta_price_time_slot_response_dto_from_dict = DeltaPriceTimeSlotResponseDto.from_dict(delta_price_time_slot_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


