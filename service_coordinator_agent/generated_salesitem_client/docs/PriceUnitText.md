# PriceUnitText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**factor_imperial** | **float** |  | [optional] 
**factor_metric** | **float** |  | [optional] 
**language_code** | **str** |  | [optional] 
**text_imperial** | **str** |  | [optional] 
**text_metric** | **str** |  | [optional] 
**unit_imperial** | **str** |  | [optional] 
**unit_metric** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.price_unit_text import PriceUnitText

# TODO update the JSON string below
json = "{}"
# create an instance of PriceUnitText from a JSON string
price_unit_text_instance = PriceUnitText.from_json(json)
# print the JSON string representation of the object
print(PriceUnitText.to_json())

# convert the object into a dict
price_unit_text_dict = price_unit_text_instance.to_dict()
# create an instance of PriceUnitText from a dict
price_unit_text_from_dict = PriceUnitText.from_dict(price_unit_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


