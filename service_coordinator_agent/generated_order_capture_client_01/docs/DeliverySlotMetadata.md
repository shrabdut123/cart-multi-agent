# DeliverySlotMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** |  | [optional] 
**has_price_deviation** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_slot_metadata import DeliverySlotMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DeliverySlotMetadata from a JSON string
delivery_slot_metadata_instance = DeliverySlotMetadata.from_json(json)
# print the JSON string representation of the object
print(DeliverySlotMetadata.to_json())

# convert the object into a dict
delivery_slot_metadata_dict = delivery_slot_metadata_instance.to_dict()
# create an instance of DeliverySlotMetadata from a dict
delivery_slot_metadata_from_dict = DeliverySlotMetadata.from_dict(delivery_slot_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


