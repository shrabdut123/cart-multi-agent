# BusinessInfo

Extra contact details, in case of business customers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | [optional] 
**phonetic_business_name** | **str** |  | [optional] 
**organization_number** | **str** |  | [optional] 
**tax_identifier_no** | **str** |  | [optional] 
**tax_code** | **str** |  | [optional] 
**tax_code_type** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.business_info import BusinessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessInfo from a JSON string
business_info_instance = BusinessInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessInfo.to_json())

# convert the object into a dict
business_info_dict = business_info_instance.to_dict()
# create an instance of BusinessInfo from a dict
business_info_from_dict = BusinessInfo.from_dict(business_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


