# SubTypeDto

It describes the sub types. It is applicable for COLLECT as COLLECt has multiple sub types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | It describes the second level category PUP, PUOP, LOCKER, CLICK_COLLECT_STORE etc | [optional] 
**max_collection_points** | **str** | It describes the max number of collection points under each sub type | [optional] 

## Example

```python
from order_capture_client.models.sub_type_dto import SubTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubTypeDto from a JSON string
sub_type_dto_instance = SubTypeDto.from_json(json)
# print the JSON string representation of the object
print(SubTypeDto.to_json())

# convert the object into a dict
sub_type_dto_dict = sub_type_dto_instance.to_dict()
# create an instance of SubTypeDto from a dict
sub_type_dto_from_dict = SubTypeDto.from_dict(sub_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


