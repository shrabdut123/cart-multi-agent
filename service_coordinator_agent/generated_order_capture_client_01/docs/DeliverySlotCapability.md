# DeliverySlotCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**selected** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_slot_capability import DeliverySlotCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverySlotCapability from a JSON string
delivery_slot_capability_instance = DeliverySlotCapability.from_json(json)
# print the JSON string representation of the object
print(DeliverySlotCapability.to_json())

# convert the object into a dict
delivery_slot_capability_dict = delivery_slot_capability_instance.to_dict()
# create an instance of DeliverySlotCapability from a dict
delivery_slot_capability_from_dict = DeliverySlotCapability.from_dict(delivery_slot_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


