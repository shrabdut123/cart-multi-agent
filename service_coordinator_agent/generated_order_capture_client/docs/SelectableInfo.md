# SelectableInfo

Selectable information. It describes if a pick up point can be selected, not selected or uncertain. It will be uncertain if time window is not evaluated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectable** | **str** | It describes whether a delivery service is selectable, not selectable or uncertain about selection. It is UNCERTAIN if time window is not evaluated yet i.e. usually in collect where closest pup time windows are evaluated and others are not | [optional] 
**reason** | **List[str]** | It describes the reason for a delivery service being not selectable or uncertain | [optional] 

## Example

```python
from order_capture_client.models.selectable_info import SelectableInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SelectableInfo from a JSON string
selectable_info_instance = SelectableInfo.from_json(json)
# print the JSON string representation of the object
print(SelectableInfo.to_json())

# convert the object into a dict
selectable_info_dict = selectable_info_instance.to_dict()
# create an instance of SelectableInfo from a dict
selectable_info_from_dict = SelectableInfo.from_dict(selectable_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


