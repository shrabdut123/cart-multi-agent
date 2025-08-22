# DeliveryAreaRequest

Determines the details of delivery area. e.g zipCode, stateCode, and city

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**zip_code** | **str** |  | 
**state_code** | **str** | Mandatory for US | [optional] 
**city** | **str** |  | [optional] 
**enable_range_of_days** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_area_request import DeliveryAreaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryAreaRequest from a JSON string
delivery_area_request_instance = DeliveryAreaRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveryAreaRequest.to_json())

# convert the object into a dict
delivery_area_request_dict = delivery_area_request_instance.to_dict()
# create an instance of DeliveryAreaRequest from a dict
delivery_area_request_from_dict = DeliveryAreaRequest.from_dict(delivery_area_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


