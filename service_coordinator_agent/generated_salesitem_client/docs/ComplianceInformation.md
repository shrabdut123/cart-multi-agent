# ComplianceInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sections** | [**List[ComplianceInformationSection]**](ComplianceInformationSection.md) |  | 
**type** | **str** |  | 

## Example

```python
from salesitem_client.models.compliance_information import ComplianceInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceInformation from a JSON string
compliance_information_instance = ComplianceInformation.from_json(json)
# print the JSON string representation of the object
print(ComplianceInformation.to_json())

# convert the object into a dict
compliance_information_dict = compliance_information_instance.to_dict()
# create an instance of ComplianceInformation from a dict
compliance_information_from_dict = ComplianceInformation.from_dict(compliance_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


