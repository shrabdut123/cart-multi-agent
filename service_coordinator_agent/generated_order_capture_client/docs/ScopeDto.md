# ScopeDto

It describes the scope that which the request was operated on i.e. list of service types requested and max collection points

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | It describes the super type HOME DELIVERY OR COLLECT | [optional] 
**sub_types** | [**List[SubTypeDto]**](SubTypeDto.md) | It describes the sub types. It is applicable for COLLECT as COLLECt has multiple sub types | [optional] 

## Example

```python
from order_capture_client.models.scope_dto import ScopeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeDto from a JSON string
scope_dto_instance = ScopeDto.from_json(json)
# print the JSON string representation of the object
print(ScopeDto.to_json())

# convert the object into a dict
scope_dto_dict = scope_dto_instance.to_dict()
# create an instance of ScopeDto from a dict
scope_dto_from_dict = ScopeDto.from_dict(scope_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


