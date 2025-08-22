# SpeInfoMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_type** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 
**message_text** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.spe_info_message import SpeInfoMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SpeInfoMessage from a JSON string
spe_info_message_instance = SpeInfoMessage.from_json(json)
# print the JSON string representation of the object
print(SpeInfoMessage.to_json())

# convert the object into a dict
spe_info_message_dict = spe_info_message_instance.to_dict()
# create an instance of SpeInfoMessage from a dict
spe_info_message_from_dict = SpeInfoMessage.from_dict(spe_info_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


