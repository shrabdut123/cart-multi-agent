# RequiredTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**included_in_package** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.required_tool import RequiredTool

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredTool from a JSON string
required_tool_instance = RequiredTool.from_json(json)
# print the JSON string representation of the object
print(RequiredTool.to_json())

# convert the object into a dict
required_tool_dict = required_tool_instance.to_dict()
# create an instance of RequiredTool from a dict
required_tool_from_dict = RequiredTool.from_dict(required_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


