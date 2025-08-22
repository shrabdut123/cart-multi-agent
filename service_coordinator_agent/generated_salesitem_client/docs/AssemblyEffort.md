# AssemblyEffort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_time** | [**EstimatedTime**](EstimatedTime.md) |  | [optional] 
**required_persons** | **int** |  | [optional] 
**required_tools** | [**List[RequiredTool]**](RequiredTool.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.assembly_effort import AssemblyEffort

# TODO update the JSON string below
json = "{}"
# create an instance of AssemblyEffort from a JSON string
assembly_effort_instance = AssemblyEffort.from_json(json)
# print the JSON string representation of the object
print(AssemblyEffort.to_json())

# convert the object into a dict
assembly_effort_dict = assembly_effort_instance.to_dict()
# create an instance of AssemblyEffort from a dict
assembly_effort_from_dict = AssemblyEffort.from_dict(assembly_effort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


