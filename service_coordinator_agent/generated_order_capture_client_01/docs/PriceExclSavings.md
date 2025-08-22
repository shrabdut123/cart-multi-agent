# PriceExclSavings

It represents the price that is exclusive savings. The definition of properties underneath this object remain same but the exception is that the values are exclusive savings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incl_tax** | **float** |  | [optional] 
**excl_tax** | **float** |  | [optional] 
**tax** | **float** |  | [optional] 
**tax_list** | [**List[Tax]**](Tax.md) |  | [optional] 
**tax_summary_list** | [**List[SpeTaxSummary]**](SpeTaxSummary.md) |  | [optional] 

## Example

```python
from order_capture_client.models.price_excl_savings import PriceExclSavings

# TODO update the JSON string below
json = "{}"
# create an instance of PriceExclSavings from a JSON string
price_excl_savings_instance = PriceExclSavings.from_json(json)
# print the JSON string representation of the object
print(PriceExclSavings.to_json())

# convert the object into a dict
price_excl_savings_dict = price_excl_savings_instance.to_dict()
# create an instance of PriceExclSavings from a dict
price_excl_savings_from_dict = PriceExclSavings.from_dict(price_excl_savings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


