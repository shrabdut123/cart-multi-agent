# DeliveryServiceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DSMetadataDto**](DSMetadataDto.md) |  | [optional] 
**id** | **str** | Order capture generated UUID | [optional] 
**delivery_arrangements_id** | **str** | iSOM provided identifier for delivery arrangement | [optional] 
**fulfillment_method_type** | **str** | HOME_DELIVERY only in case type is HOME_DELIVERY and rest others if type is COLLECT | [optional] 
**fulfillment_possibility** | **str** | This describes whether it can fulfill complete cart, partial or cannot fulfill due to complete unavailability. FULL - All items are available, NONE - No items are available and this is only for CLICK_COLLECT_STORE as of now, PARTIAL - Few are available | [optional] 
**solution_id** | **str** | iSOM provided identifier for a delivery solution | [optional] 
**solution** | **str** | It defines the delivery solution. HOME_DELIVERY has STANDARD, CURBSIDE, EXPRESS_CURBSIDE, EXPRESS, STANDARD_RD, CURBSIDE_RD, EXPRESS_CURBSIDE_RD, EXPRESS_RD. COLLECT has STANDARD and sometimes LOCKER for Internal lockers | [optional] 
**solution_price** | [**DeliveryServicePriceDto**](DeliveryServicePriceDto.md) |  | [optional] 
**expiry_time** | **str** | Defines how long this delivery is kept without re-calculating with iSOM | [optional] 
**possible_deliveries** | [**PossibleDeliveriesDto**](PossibleDeliveriesDto.md) |  | [optional] 
**errors** | [**List[ErrorDto]**](ErrorDto.md) | It contains a list of different errors that could possibly impact this as a choice of selection. The metadata has information that helps decide the presentation | [optional] 
**unavailable_items** | [**List[UnavailableItemDto]**](UnavailableItemDto.md) | It contains a list of unavailable items for a delivery service with a reason of unavailability | [optional] 

## Example

```python
from order_capture_client.models.delivery_service_dto import DeliveryServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryServiceDto from a JSON string
delivery_service_dto_instance = DeliveryServiceDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryServiceDto.to_json())

# convert the object into a dict
delivery_service_dto_dict = delivery_service_dto_instance.to_dict()
# create an instance of DeliveryServiceDto from a dict
delivery_service_dto_from_dict = DeliveryServiceDto.from_dict(delivery_service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


