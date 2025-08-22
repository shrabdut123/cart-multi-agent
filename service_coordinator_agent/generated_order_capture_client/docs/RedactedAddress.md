# RedactedAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redacted_zip_code** | **str** |  | 
**state_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.redacted_address import RedactedAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RedactedAddress from a JSON string
redacted_address_instance = RedactedAddress.from_json(json)
# print the JSON string representation of the object
print(RedactedAddress.to_json())

# convert the object into a dict
redacted_address_dict = redacted_address_instance.to_dict()
# create an instance of RedactedAddress from a dict
redacted_address_from_dict = RedactedAddress.from_dict(redacted_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


