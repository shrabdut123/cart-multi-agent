# DeliveryServiceEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**delivery_arrangements_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**fulfillment_method_type** | **str** |  | [optional] 
**solution_id** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**solution_price** | [**Price**](Price.md) |  | [optional] 
**price_override_reference** | **float** |  | [optional] 
**expiry_time** | **str** |  | [optional] 
**deliveries** | [**List[DeliveryEntity]**](DeliveryEntity.md) |  | [optional] 
**wheel_chair_capability** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_service_entity import DeliveryServiceEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryServiceEntity from a JSON string
delivery_service_entity_instance = DeliveryServiceEntity.from_json(json)
# print the JSON string representation of the object
print(DeliveryServiceEntity.to_json())

# convert the object into a dict
delivery_service_entity_dict = delivery_service_entity_instance.to_dict()
# create an instance of DeliveryServiceEntity from a dict
delivery_service_entity_from_dict = DeliveryServiceEntity.from_dict(delivery_service_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


