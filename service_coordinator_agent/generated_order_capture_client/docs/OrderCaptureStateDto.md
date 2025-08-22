# OrderCaptureStateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_price** | [**Price**](Price.md) |  | [optional] 
**service_price** | [**Price**](Price.md) |  | [optional] 
**goods_total** | [**Price**](Price.md) |  | [optional] 
**order_total** | [**Price**](Price.md) |  | [optional] 
**state** | **str** |  | [optional] 
**service_offers** | [**List[ServiceOffer]**](ServiceOffer.md) |  | [optional] 

## Example

```python
from order_capture_client.models.order_capture_state_dto import OrderCaptureStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCaptureStateDto from a JSON string
order_capture_state_dto_instance = OrderCaptureStateDto.from_json(json)
# print the JSON string representation of the object
print(OrderCaptureStateDto.to_json())

# convert the object into a dict
order_capture_state_dto_dict = order_capture_state_dto_instance.to_dict()
# create an instance of OrderCaptureStateDto from a dict
order_capture_state_dto_from_dict = OrderCaptureStateDto.from_dict(order_capture_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


