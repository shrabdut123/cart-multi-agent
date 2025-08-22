# TechnicalInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**information_groups** | [**List[TechnicalInformationGroup]**](TechnicalInformationGroup.md) |  | 

## Example

```python
from salesitem_client.models.technical_information import TechnicalInformation

# TODO update the JSON string below
json = "{}"
# create an instance of TechnicalInformation from a JSON string
technical_information_instance = TechnicalInformation.from_json(json)
# print the JSON string representation of the object
print(TechnicalInformation.to_json())

# convert the object into a dict
technical_information_dict = technical_information_instance.to_dict()
# create an instance of TechnicalInformation from a dict
technical_information_from_dict = TechnicalInformation.from_dict(technical_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


