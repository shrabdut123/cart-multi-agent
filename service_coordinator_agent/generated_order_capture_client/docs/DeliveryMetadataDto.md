# DeliveryMetadataDto

Informational node. It contains metadata about delivery such as multiple deliveries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_of_days** | **bool** |  | [optional] 
**no_stock_delivery** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.delivery_metadata_dto import DeliveryMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryMetadataDto from a JSON string
delivery_metadata_dto_instance = DeliveryMetadataDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryMetadataDto.to_json())

# convert the object into a dict
delivery_metadata_dto_dict = delivery_metadata_dto_instance.to_dict()
# create an instance of DeliveryMetadataDto from a dict
delivery_metadata_dto_from_dict = DeliveryMetadataDto.from_dict(delivery_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


