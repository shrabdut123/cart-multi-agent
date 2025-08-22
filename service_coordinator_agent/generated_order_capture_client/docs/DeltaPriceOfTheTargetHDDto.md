# DeltaPriceOfTheTargetHDDto

It gives the calculated delta prices of the timewindow slots under target delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **str** | It represents the target delivery id for which we need to calculate the delta prices for | [optional] 
**fulfillment_delivery_id** | **str** | It represents the target delivery fulfilment id for which we need to calculate the delta prices for | [optional] 
**delivery_service_item_number** | **str** | It represents the target delivery serviceItem number for which we need to calculate the delta prices for | [optional] 
**delivery_tw_slots_of_target_delivery** | [**DeliveryTimeWindowsOfTargetHDDto**](DeliveryTimeWindowsOfTargetHDDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delta_price_of_the_target_hd_dto import DeltaPriceOfTheTargetHDDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaPriceOfTheTargetHDDto from a JSON string
delta_price_of_the_target_hd_dto_instance = DeltaPriceOfTheTargetHDDto.from_json(json)
# print the JSON string representation of the object
print(DeltaPriceOfTheTargetHDDto.to_json())

# convert the object into a dict
delta_price_of_the_target_hd_dto_dict = delta_price_of_the_target_hd_dto_instance.to_dict()
# create an instance of DeltaPriceOfTheTargetHDDto from a dict
delta_price_of_the_target_hd_dto_from_dict = DeltaPriceOfTheTargetHDDto.from_dict(delta_price_of_the_target_hd_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


