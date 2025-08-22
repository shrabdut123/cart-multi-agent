# CapabilityDto

It describes the different supported capabilities such as AUTH_TO_LEAVE, WHEELCHAIR etc. It does not mean it is available

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wheel_chair** | **bool** |  | [optional] 
**range_of_days** | **bool** |  | [optional] 
**auth_to_leave** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.capability_dto import CapabilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilityDto from a JSON string
capability_dto_instance = CapabilityDto.from_json(json)
# print the JSON string representation of the object
print(CapabilityDto.to_json())

# convert the object into a dict
capability_dto_dict = capability_dto_instance.to_dict()
# create an instance of CapabilityDto from a dict
capability_dto_from_dict = CapabilityDto.from_dict(capability_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


