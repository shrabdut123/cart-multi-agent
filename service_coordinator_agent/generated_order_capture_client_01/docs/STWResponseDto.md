# STWResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**STWContextDto**](STWContextDto.md) |  | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**possible_service_time_windows** | [**PossibleServiceTimeWindowsDto**](PossibleServiceTimeWindowsDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.stw_response_dto import STWResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of STWResponseDto from a JSON string
stw_response_dto_instance = STWResponseDto.from_json(json)
# print the JSON string representation of the object
print(STWResponseDto.to_json())

# convert the object into a dict
stw_response_dto_dict = stw_response_dto_instance.to_dict()
# create an instance of STWResponseDto from a dict
stw_response_dto_from_dict = STWResponseDto.from_dict(stw_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


