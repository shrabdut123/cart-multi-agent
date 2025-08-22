# PossiblePickUpPointPricesOfOtherDeliveryDto

It gives the list of PUP's in the target delivery with the delta prices and actual discounted prices of PUP's

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | iSOM provided ID for a pick up point | [optional] 
**pick_up_point_prices** | [**List[PickUpPointPriceDeltaDto]**](PickUpPointPriceDeltaDto.md) | It is for future use | [optional] 

## Example

```python
from order_capture_client.models.possible_pick_up_point_prices_of_other_delivery_dto import PossiblePickUpPointPricesOfOtherDeliveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossiblePickUpPointPricesOfOtherDeliveryDto from a JSON string
possible_pick_up_point_prices_of_other_delivery_dto_instance = PossiblePickUpPointPricesOfOtherDeliveryDto.from_json(json)
# print the JSON string representation of the object
print(PossiblePickUpPointPricesOfOtherDeliveryDto.to_json())

# convert the object into a dict
possible_pick_up_point_prices_of_other_delivery_dto_dict = possible_pick_up_point_prices_of_other_delivery_dto_instance.to_dict()
# create an instance of PossiblePickUpPointPricesOfOtherDeliveryDto from a dict
possible_pick_up_point_prices_of_other_delivery_dto_from_dict = PossiblePickUpPointPricesOfOtherDeliveryDto.from_dict(possible_pick_up_point_prices_of_other_delivery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


