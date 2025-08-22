# SelectedDeliveryServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_service_id** | **str** | It refers to the selected delivery service ID | 
**selected_deliveries** | [**List[SelectedDeliveryReq]**](SelectedDeliveryReq.md) |  | [optional] 
**target_delivery_id** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.selected_delivery_service_request import SelectedDeliveryServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedDeliveryServiceRequest from a JSON string
selected_delivery_service_request_instance = SelectedDeliveryServiceRequest.from_json(json)
# print the JSON string representation of the object
print(SelectedDeliveryServiceRequest.to_json())

# convert the object into a dict
selected_delivery_service_request_dict = selected_delivery_service_request_instance.to_dict()
# create an instance of SelectedDeliveryServiceRequest from a dict
selected_delivery_service_request_from_dict = SelectedDeliveryServiceRequest.from_dict(selected_delivery_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


