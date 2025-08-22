# TechnicalCompliance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heading** | **str** |  | [optional] 
**heading_global** | **str** |  | [optional] 
**heading_type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.technical_compliance import TechnicalCompliance

# TODO update the JSON string below
json = "{}"
# create an instance of TechnicalCompliance from a JSON string
technical_compliance_instance = TechnicalCompliance.from_json(json)
# print the JSON string representation of the object
print(TechnicalCompliance.to_json())

# convert the object into a dict
technical_compliance_dict = technical_compliance_instance.to_dict()
# create an instance of TechnicalCompliance from a dict
technical_compliance_from_dict = TechnicalCompliance.from_dict(technical_compliance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


