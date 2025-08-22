# TechnicalInformationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heading_no** | **str** |  | 
**heading_text** | **str** |  | 
**information_parts** | [**List[TechnicalInformationPart]**](TechnicalInformationPart.md) |  | [optional] 

## Example

```python
from salesitem_client.models.technical_information_group import TechnicalInformationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TechnicalInformationGroup from a JSON string
technical_information_group_instance = TechnicalInformationGroup.from_json(json)
# print the JSON string representation of the object
print(TechnicalInformationGroup.to_json())

# convert the object into a dict
technical_information_group_dict = technical_information_group_instance.to_dict()
# create an instance of TechnicalInformationGroup from a dict
technical_information_group_from_dict = TechnicalInformationGroup.from_dict(technical_information_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


