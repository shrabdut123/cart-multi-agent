# FullLengthText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_id** | **str** |  | [optional] 
**texts** | [**List[FullLengthTextDetailed]**](FullLengthTextDetailed.md) |  | [optional] 

## Example

```python
from salesitem_client.models.full_length_text import FullLengthText

# TODO update the JSON string below
json = "{}"
# create an instance of FullLengthText from a JSON string
full_length_text_instance = FullLengthText.from_json(json)
# print the JSON string representation of the object
print(FullLengthText.to_json())

# convert the object into a dict
full_length_text_dict = full_length_text_instance.to_dict()
# create an instance of FullLengthText from a dict
full_length_text_from_dict = FullLengthText.from_dict(full_length_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


