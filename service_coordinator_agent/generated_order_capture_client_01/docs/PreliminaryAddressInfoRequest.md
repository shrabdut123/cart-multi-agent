# PreliminaryAddressInfoRequest

This field is not mandatory. If provided, it should represent shipping information. This information provided can be leveraged as billing information for COLLECT if the address happens to the same for both billing and shipping. The child properties are validated if provided. This information will not create an address. It will be echoed back on a GET which consumers can leverage to present or pre-fill in the required situations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | It will be validated against retail unit expectations inherited from address validations. It will be echoed back if it was provided as input | [optional] 
**address_line2** | **str** | It will be validated against retail unit expectations inherited from address validations. It will be echoed back if it was provided as input | [optional] 
**address_line3** | **str** | It will be validated against retail unit expectations inherited from address validations.  It will be echoed back if it was provided as input | [optional] 
**city** | **str** | It will be validated against retail unit expectations inherited from address validations.  It will be echoed back if it was provided as input | [optional] 
**zip_code** | **str** | It will be validated against retail unit expectations inherited from address validations.  It will be echoed back if it was provided as input | [optional] 
**state_code** | **str** | It will be validated against retail unit expectations inherited from address validations. This state code should be the standard ISO codes with either 2 or 3 characters. It will be echoed back if it was provided as input | [optional] 

## Example

```python
from order_capture_client.models.preliminary_address_info_request import PreliminaryAddressInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreliminaryAddressInfoRequest from a JSON string
preliminary_address_info_request_instance = PreliminaryAddressInfoRequest.from_json(json)
# print the JSON string representation of the object
print(PreliminaryAddressInfoRequest.to_json())

# convert the object into a dict
preliminary_address_info_request_dict = preliminary_address_info_request_instance.to_dict()
# create an instance of PreliminaryAddressInfoRequest from a dict
preliminary_address_info_request_from_dict = PreliminaryAddressInfoRequest.from_dict(preliminary_address_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


