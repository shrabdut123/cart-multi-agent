# ComplianceUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.compliance_url import ComplianceUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceUrl from a JSON string
compliance_url_instance = ComplianceUrl.from_json(json)
# print the JSON string representation of the object
print(ComplianceUrl.to_json())

# convert the object into a dict
compliance_url_dict = compliance_url_instance.to_dict()
# create an instance of ComplianceUrl from a dict
compliance_url_from_dict = ComplianceUrl.from_dict(compliance_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


