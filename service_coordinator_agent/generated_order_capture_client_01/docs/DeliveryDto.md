# DeliveryDto

List of delivery and its details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order capture generated UUID for a delivery | [optional] 
**metadata** | [**DeliveryMetadataDto**](DeliveryMetadataDto.md) |  | [optional] 
**fulfillment_delivery_id** | **str** | iSOM generated delivery Id | [optional] 
**service_item_id** | **str** | It is a delivery identifier. This number translates to an unique delivery i.e. standard home delivery truck for example. This may not be an useful information for display and it is required for order creation and debugging purpose | [optional] 
**type** | **str** | Translation of SGR. It is not a full translation but it distinguish between PARCEL, TRUCK | [optional] 
**delivery_price** | [**DeliveryServicePriceDto**](DeliveryServicePriceDto.md) |  | [optional] 
**delivery_items** | [**List[DeliveryItemDto]**](DeliveryItemDto.md) | It contains a list of item complex types that are part of the delivery. At times, the orders are split into more than 1 delivery. This node provides information about items that are grouped under each delivery | [optional] 
**possible_pick_up_points** | [**PossiblePickUpPointsDto**](PossiblePickUpPointsDto.md) |  | [optional] 
**time_windows** | [**TimeWindowsDto**](TimeWindowsDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_dto import DeliveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryDto from a JSON string
delivery_dto_instance = DeliveryDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryDto.to_json())

# convert the object into a dict
delivery_dto_dict = delivery_dto_instance.to_dict()
# create an instance of DeliveryDto from a dict
delivery_dto_from_dict = DeliveryDto.from_dict(delivery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


