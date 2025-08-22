# CreateUpdateDSResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_service** | [**DeliveryServiceEntity**](DeliveryServiceEntity.md) |  | [optional] 
**services_and_time_windows** | [**List[ServiceAndTimeWindowsEntity]**](ServiceAndTimeWindowsEntity.md) |  | [optional] 
**order_capture_state** | [**OrderCaptureStateDto**](OrderCaptureStateDto.md) |  | [optional] 
**error** | [**ErrorDto**](ErrorDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.create_update_ds_response_dto import CreateUpdateDSResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateDSResponseDto from a JSON string
create_update_ds_response_dto_instance = CreateUpdateDSResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateDSResponseDto.to_json())

# convert the object into a dict
create_update_ds_response_dto_dict = create_update_ds_response_dto_instance.to_dict()
# create an instance of CreateUpdateDSResponseDto from a dict
create_update_ds_response_dto_from_dict = CreateUpdateDSResponseDto.from_dict(create_update_ds_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


