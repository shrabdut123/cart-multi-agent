# ErrorDetailDto

It describes the external error in detail if external. Otherwise internal error details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Either an external system error code if external integration error or internal error code if internal exception | [optional] 
**error_description** | **str** | Either an external system error description if external integration error or internal error description if internal exception | [optional] 
**error_unique_exception_id** | **str** | Either an external unique identifier for error if external integration error or internal identifier | [optional] 

## Example

```python
from order_capture_client.models.error_detail_dto import ErrorDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailDto from a JSON string
error_detail_dto_instance = ErrorDetailDto.from_json(json)
# print the JSON string representation of the object
print(ErrorDetailDto.to_json())

# convert the object into a dict
error_detail_dto_dict = error_detail_dto_instance.to_dict()
# create an instance of ErrorDetailDto from a dict
error_detail_dto_from_dict = ErrorDetailDto.from_dict(error_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


