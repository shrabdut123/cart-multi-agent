# SOPlatformCreateInfoDto

This property is available if the status is CREATED. For other status, this property will be empty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_draft_url** | **str** | This is the job URL created by Service Offer. This can be used by customers to view their service quote | [optional] 
**service_area** | [**ServiceAreaDto**](ServiceAreaDto.md) |  | [optional] 
**service_items** | [**List[ServiceItemDto]**](ServiceItemDto.md) | This contains the list of services requested along with its details | [optional] 

## Example

```python
from order_capture_client.models.so_platform_create_info_dto import SOPlatformCreateInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of SOPlatformCreateInfoDto from a JSON string
so_platform_create_info_dto_instance = SOPlatformCreateInfoDto.from_json(json)
# print the JSON string representation of the object
print(SOPlatformCreateInfoDto.to_json())

# convert the object into a dict
so_platform_create_info_dto_dict = so_platform_create_info_dto_instance.to_dict()
# create an instance of SOPlatformCreateInfoDto from a dict
so_platform_create_info_dto_from_dict = SOPlatformCreateInfoDto.from_dict(so_platform_create_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


