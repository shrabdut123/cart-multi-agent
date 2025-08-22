# RemovalServiceItemRequest

List of selling services associated with the order, mandatory if a cart having both goods items and             service items that needs to be captured

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_item_no** | **str** | It identifies a service item. Usually a string starting with SGR for IKEA, TASKRABBIT for TASKRABBIT provider | [optional] 
**service_product_id** | **str** | It identifies a service product | [optional] 
**provider** | **str** | It identifies the type of provider i.e. IKEA or TASKRABBIT for example | [optional] 
**pay_to_provider** | **bool** | It indicate if the payment is towards IKEA or external service provider | [optional] 
**quantity** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.removal_service_item_request import RemovalServiceItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalServiceItemRequest from a JSON string
removal_service_item_request_instance = RemovalServiceItemRequest.from_json(json)
# print the JSON string representation of the object
print(RemovalServiceItemRequest.to_json())

# convert the object into a dict
removal_service_item_request_dict = removal_service_item_request_instance.to_dict()
# create an instance of RemovalServiceItemRequest from a dict
removal_service_item_request_from_dict = RemovalServiceItemRequest.from_dict(removal_service_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


