# ComplianceInformationSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heading** | **str** |  | [optional] 
**urls** | [**List[ComplianceUrl]**](ComplianceUrl.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from salesitem_client.models.compliance_information_section import ComplianceInformationSection

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceInformationSection from a JSON string
compliance_information_section_instance = ComplianceInformationSection.from_json(json)
# print the JSON string representation of the object
print(ComplianceInformationSection.to_json())

# convert the object into a dict
compliance_information_section_dict = compliance_information_section_instance.to_dict()
# create an instance of ComplianceInformationSection from a dict
compliance_information_section_from_dict = ComplianceInformationSection.from_dict(compliance_information_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


