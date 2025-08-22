# SOPlatformCreateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | This property indicates the status of quote create. In async mode, if the status is available, then it will be COMPLETED. Otherwise it will be PENDING until a timeout and TIME_OUT if there is no result for a configured interval | 
**platform_create_info** | [**SOPlatformCreateInfoDto**](SOPlatformCreateInfoDto.md) |  | [optional] 
**errors** | [**List[SOErrorDto]**](SOErrorDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.so_platform_create_response_dto import SOPlatformCreateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SOPlatformCreateResponseDto from a JSON string
so_platform_create_response_dto_instance = SOPlatformCreateResponseDto.from_json(json)
# print the JSON string representation of the object
print(SOPlatformCreateResponseDto.to_json())

# convert the object into a dict
so_platform_create_response_dto_dict = so_platform_create_response_dto_instance.to_dict()
# create an instance of SOPlatformCreateResponseDto from a dict
so_platform_create_response_dto_from_dict = SOPlatformCreateResponseDto.from_dict(so_platform_create_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


