# DeltaPriceResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_delivery_service_delta_dto** | [**SelectedDeliveryServiceDeltaDto**](SelectedDeliveryServiceDeltaDto.md) |  | [optional] 
**possible_pick_up_point_prices_of_other_delivery_dto** | [**PossiblePickUpPointPricesOfOtherDeliveryDto**](PossiblePickUpPointPricesOfOtherDeliveryDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delta_price_response_dto import DeltaPriceResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeltaPriceResponseDto from a JSON string
delta_price_response_dto_instance = DeltaPriceResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeltaPriceResponseDto.to_json())

# convert the object into a dict
delta_price_response_dto_dict = delta_price_response_dto_instance.to_dict()
# create an instance of DeltaPriceResponseDto from a dict
delta_price_response_dto_from_dict = DeltaPriceResponseDto.from_dict(delta_price_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


