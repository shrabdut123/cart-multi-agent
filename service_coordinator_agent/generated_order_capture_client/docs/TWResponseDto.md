# TWResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**TWContextDto**](TWContextDto.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**possible_delivery_time_windows** | [**PossibleDeliveryTimeWindowsDto**](PossibleDeliveryTimeWindowsDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.tw_response_dto import TWResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TWResponseDto from a JSON string
tw_response_dto_instance = TWResponseDto.from_json(json)
# print the JSON string representation of the object
print(TWResponseDto.to_json())

# convert the object into a dict
tw_response_dto_dict = tw_response_dto_instance.to_dict()
# create an instance of TWResponseDto from a dict
tw_response_dto_from_dict = TWResponseDto.from_dict(tw_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


