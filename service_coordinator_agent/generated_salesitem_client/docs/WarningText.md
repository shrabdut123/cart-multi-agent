# WarningText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**urls** | [**List[WarningUrl]**](WarningUrl.md) |  | [optional] 

## Example

```python
from salesitem_client.models.warning_text import WarningText

# TODO update the JSON string below
json = "{}"
# create an instance of WarningText from a JSON string
warning_text_instance = WarningText.from_json(json)
# print the JSON string representation of the object
print(WarningText.to_json())

# convert the object into a dict
warning_text_dict = warning_text_instance.to_dict()
# create an instance of WarningText from a dict
warning_text_from_dict = WarningText.from_dict(warning_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


