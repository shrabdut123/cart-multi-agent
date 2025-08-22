# DeliveryAndServiceEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_and_service_id** | **str** |  | [optional] 
**delivery_service** | [**DeliveryServiceEntity**](DeliveryServiceEntity.md) |  | [optional] 
**service_and_time_windows** | [**List[ServiceAndTimeWindowsEntity]**](ServiceAndTimeWindowsEntity.md) |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_and_service_entity import DeliveryAndServiceEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryAndServiceEntity from a JSON string
delivery_and_service_entity_instance = DeliveryAndServiceEntity.from_json(json)
# print the JSON string representation of the object
print(DeliveryAndServiceEntity.to_json())

# convert the object into a dict
delivery_and_service_entity_dict = delivery_and_service_entity_instance.to_dict()
# create an instance of DeliveryAndServiceEntity from a dict
delivery_and_service_entity_from_dict = DeliveryAndServiceEntity.from_dict(delivery_and_service_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


