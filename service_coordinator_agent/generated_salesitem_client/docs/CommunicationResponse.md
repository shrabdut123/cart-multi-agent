# CommunicationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ItemCommunication]**](ItemCommunication.md) |  | 
**error** | [**Status**](Status.md) |  | [optional] 
**trace_id** | **str** | The unique ID connected to this specific request. Can be used by support to trace the error | [optional] 

## Example

```python
from salesitem_client.models.communication_response import CommunicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationResponse from a JSON string
communication_response_instance = CommunicationResponse.from_json(json)
# print the JSON string representation of the object
print(CommunicationResponse.to_json())

# convert the object into a dict
communication_response_dict = communication_response_instance.to_dict()
# create an instance of CommunicationResponse from a dict
communication_response_from_dict = CommunicationResponse.from_dict(communication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


