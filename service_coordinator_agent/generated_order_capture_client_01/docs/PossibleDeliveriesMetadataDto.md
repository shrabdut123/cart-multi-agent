# PossibleDeliveriesMetadataDto

Describes delivery metadata. Informational attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiple_deliveries** | **bool** | It will be true if the order is grouped into more than 1 delivery. Otherwise it will be false | [optional] 

## Example

```python
from order_capture_client.models.possible_deliveries_metadata_dto import PossibleDeliveriesMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleDeliveriesMetadataDto from a JSON string
possible_deliveries_metadata_dto_instance = PossibleDeliveriesMetadataDto.from_json(json)
# print the JSON string representation of the object
print(PossibleDeliveriesMetadataDto.to_json())

# convert the object into a dict
possible_deliveries_metadata_dto_dict = possible_deliveries_metadata_dto_instance.to_dict()
# create an instance of PossibleDeliveriesMetadataDto from a dict
possible_deliveries_metadata_dto_from_dict = PossibleDeliveriesMetadataDto.from_dict(possible_deliveries_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


