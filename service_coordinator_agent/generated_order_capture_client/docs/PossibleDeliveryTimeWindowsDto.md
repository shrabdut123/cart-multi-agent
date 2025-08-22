# PossibleDeliveryTimeWindowsDto

It describes the time windows and its additional properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**DeliveryTimeWindowsMetadataDto**](DeliveryTimeWindowsMetadataDto.md) |  | [optional] 
**time_windows** | [**List[PossibleDeliveryTimeWindowDto]**](PossibleDeliveryTimeWindowDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.possible_delivery_time_windows_dto import PossibleDeliveryTimeWindowsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PossibleDeliveryTimeWindowsDto from a JSON string
possible_delivery_time_windows_dto_instance = PossibleDeliveryTimeWindowsDto.from_json(json)
# print the JSON string representation of the object
print(PossibleDeliveryTimeWindowsDto.to_json())

# convert the object into a dict
possible_delivery_time_windows_dto_dict = possible_delivery_time_windows_dto_instance.to_dict()
# create an instance of PossibleDeliveryTimeWindowsDto from a dict
possible_delivery_time_windows_dto_from_dict = PossibleDeliveryTimeWindowsDto.from_dict(possible_delivery_time_windows_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


