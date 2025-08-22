# TechnicalInformationPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explanatory_text** | **str** |  | [optional] 
**legal** | **bool** |  | 
**range_no** | **str** |  | 
**range_text** | **str** |  | [optional] 
**text** | **str** |  | 
**text_imperial** | **str** |  | [optional] 
**text_metric** | **str** |  | [optional] 
**text_no** | **str** |  | 
**unit_imperial** | **str** |  | [optional] 
**unit_metric** | **str** |  | [optional] 
**value_imperial** | **str** |  | [optional] 
**value_metric** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.technical_information_part import TechnicalInformationPart

# TODO update the JSON string below
json = "{}"
# create an instance of TechnicalInformationPart from a JSON string
technical_information_part_instance = TechnicalInformationPart.from_json(json)
# print the JSON string representation of the object
print(TechnicalInformationPart.to_json())

# convert the object into a dict
technical_information_part_dict = technical_information_part_instance.to_dict()
# create an instance of TechnicalInformationPart from a dict
technical_information_part_from_dict = TechnicalInformationPart.from_dict(technical_information_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


