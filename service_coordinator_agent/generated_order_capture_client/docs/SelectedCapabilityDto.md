# SelectedCapabilityDto

The capabilities if relevant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wheel_chair** | **bool** | This should be set to true only if the selected solution has this enabled | [optional] 
**auth_to_leave** | **bool** | This should be set to true only if the selected time window has that capability | [optional] 

## Example

```python
from order_capture_client.models.selected_capability_dto import SelectedCapabilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedCapabilityDto from a JSON string
selected_capability_dto_instance = SelectedCapabilityDto.from_json(json)
# print the JSON string representation of the object
print(SelectedCapabilityDto.to_json())

# convert the object into a dict
selected_capability_dto_dict = selected_capability_dto_instance.to_dict()
# create an instance of SelectedCapabilityDto from a dict
selected_capability_dto_from_dict = SelectedCapabilityDto.from_dict(selected_capability_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


