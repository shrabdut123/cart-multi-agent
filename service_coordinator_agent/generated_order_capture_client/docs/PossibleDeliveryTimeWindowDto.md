# PossibleDeliveryTimeWindowDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DeliveryTimeWindowMetadataDto**](DeliveryTimeWindowMetadataDto.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**delivery_id** | **str** | OC generated delivery identifier | [optional] 
**fulfillment_delivery_id** | **str** | CCS~~~8 | [optional] 
**delivery_service_item_number** | **str** | iSOM provided service item number | [optional] 
**pick_up_point_identifier** | **str** | iSOM provided pick up point identifier. It is not ID and it is identifier | [optional] 
**oc_pupid** | **str** | It describes the order capture generated UUID for a pick up point | [optional] 
**delivery_time_windows** | [**TWPossibleSlotsDto**](TWPossibleSlotsDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.possible_delivery_time_window_dto import PossibleDeliveryTimeWindowDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleDeliveryTimeWindowDto from a JSON string
possible_delivery_time_window_dto_instance = PossibleDeliveryTimeWindowDto.from_json(json)
# print the JSON string representation of the object
print(PossibleDeliveryTimeWindowDto.to_json())

# convert the object into a dict
possible_delivery_time_window_dto_dict = possible_delivery_time_window_dto_instance.to_dict()
# create an instance of PossibleDeliveryTimeWindowDto from a dict
possible_delivery_time_window_dto_from_dict = PossibleDeliveryTimeWindowDto.from_dict(possible_delivery_time_window_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


