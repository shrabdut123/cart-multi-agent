# SOErrorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.so_error_dto import SOErrorDto

# TODO update the JSON string below
json = "{}"
# create an instance of SOErrorDto from a JSON string
so_error_dto_instance = SOErrorDto.from_json(json)
# print the JSON string representation of the object
print(SOErrorDto.to_json())

# convert the object into a dict
so_error_dto_dict = so_error_dto_instance.to_dict()
# create an instance of SOErrorDto from a dict
so_error_dto_from_dict = SOErrorDto.from_dict(so_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


