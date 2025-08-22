# ServiceTimeWindowErrorDto

It describes the list of services that has service time window failures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_item_no** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.service_time_window_error_dto import ServiceTimeWindowErrorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTimeWindowErrorDto from a JSON string
service_time_window_error_dto_instance = ServiceTimeWindowErrorDto.from_json(json)
# print the JSON string representation of the object
print(ServiceTimeWindowErrorDto.to_json())

# convert the object into a dict
service_time_window_error_dto_dict = service_time_window_error_dto_instance.to_dict()
# create an instance of ServiceTimeWindowErrorDto from a dict
service_time_window_error_dto_from_dict = ServiceTimeWindowErrorDto.from_dict(service_time_window_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


