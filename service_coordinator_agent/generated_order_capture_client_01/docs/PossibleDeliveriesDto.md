# PossibleDeliveriesDto

This node contains information about delivery. It will have time windows and also possible pick up points if the service is a collect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**PossibleDeliveriesMetadataDto**](PossibleDeliveriesMetadataDto.md) |  | [optional] 
**deliveries** | [**List[DeliveryDto]**](DeliveryDto.md) | List of delivery and its details | [optional] 

## Example

```python
from order_capture_client.models.possible_deliveries_dto import PossibleDeliveriesDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleDeliveriesDto from a JSON string
possible_deliveries_dto_instance = PossibleDeliveriesDto.from_json(json)
# print the JSON string representation of the object
print(PossibleDeliveriesDto.to_json())

# convert the object into a dict
possible_deliveries_dto_dict = possible_deliveries_dto_instance.to_dict()
# create an instance of PossibleDeliveriesDto from a dict
possible_deliveries_dto_from_dict = PossibleDeliveriesDto.from_dict(possible_deliveries_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


