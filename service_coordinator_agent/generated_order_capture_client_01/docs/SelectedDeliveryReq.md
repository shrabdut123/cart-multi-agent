# SelectedDeliveryReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **str** | It refers to the delivery id under a selected delivery service | 
**pick_up_point_id** | **str** | The selected pick up point of above delivery if the selected delivery service is a collect delivery | [optional] 
**time_window_id** | **str** | The selected time window ID of the above delivery | [optional] 

## Example

```python
from order_capture_client.models.selected_delivery_req import SelectedDeliveryReq

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedDeliveryReq from a JSON string
selected_delivery_req_instance = SelectedDeliveryReq.from_json(json)
# print the JSON string representation of the object
print(SelectedDeliveryReq.to_json())

# convert the object into a dict
selected_delivery_req_dict = selected_delivery_req_instance.to_dict()
# create an instance of SelectedDeliveryReq from a dict
selected_delivery_req_from_dict = SelectedDeliveryReq.from_dict(selected_delivery_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


