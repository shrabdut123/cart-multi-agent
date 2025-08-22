# ExceptionalScenario


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception_code** | **str** |  | [optional] 
**exception_reason** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.exceptional_scenario import ExceptionalScenario

# TODO update the JSON string below
json = "{}"
# create an instance of ExceptionalScenario from a JSON string
exceptional_scenario_instance = ExceptionalScenario.from_json(json)
# print the JSON string representation of the object
print(ExceptionalScenario.to_json())

# convert the object into a dict
exceptional_scenario_dict = exceptional_scenario_instance.to_dict()
# create an instance of ExceptionalScenario from a dict
exceptional_scenario_from_dict = ExceptionalScenario.from_dict(exceptional_scenario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


