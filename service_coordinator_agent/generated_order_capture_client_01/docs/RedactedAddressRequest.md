# RedactedAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redacted_zip_code** | **str** |  | 
**state_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.redacted_address_request import RedactedAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedactedAddressRequest from a JSON string
redacted_address_request_instance = RedactedAddressRequest.from_json(json)
# print the JSON string representation of the object
print(RedactedAddressRequest.to_json())

# convert the object into a dict
redacted_address_request_dict = redacted_address_request_instance.to_dict()
# create an instance of RedactedAddressRequest from a dict
redacted_address_request_from_dict = RedactedAddressRequest.from_dict(redacted_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


