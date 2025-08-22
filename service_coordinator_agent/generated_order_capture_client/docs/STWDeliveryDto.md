# STWDeliveryDto

The deliveries and time windows of a selected service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **str** | Order capture generated UUID for a delivery | [optional] 
**selected_delivery_time_windows_id** | **str** | It describes the selected time window id of a delivery | [optional] 
**selected_delivery_time_window_from_date_time** | **str** | It describes the selected time window of a delivery i.e. from date and time. Already adjusted to time zone | [optional] 
**selected_delivery_time_window_to_date_time** | **str** | It describes the selected time window of a delivery i.e. to date and time. Already adjusted to time zone | [optional] 
**delivery_service_item_number** | **str** | It is a delivery identifier. This number translates to an unique delivery i.e. standard home delivery truck for example. This may not be an useful information for display and it is required for order creation and debugging purpose | [optional] 
**delivery_type** | **str** | Translation of SGR. It is not a full translation but it distinguish between PARCEL, TRUCK | [optional] 

## Example

```python
from order_capture_client.models.stw_delivery_dto import STWDeliveryDto

# TODO update the JSON string below
json = "{}"
# create an instance of STWDeliveryDto from a JSON string
stw_delivery_dto_instance = STWDeliveryDto.from_json(json)
# print the JSON string representation of the object
print(STWDeliveryDto.to_json())

# convert the object into a dict
stw_delivery_dto_dict = stw_delivery_dto_instance.to_dict()
# create an instance of STWDeliveryDto from a dict
stw_delivery_dto_from_dict = STWDeliveryDto.from_dict(stw_delivery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


