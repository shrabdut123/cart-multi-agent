# SalesPriceUnitPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicative_imperial_total_tax** | **float** |  | [optional] 
**indicative_metric_total_tax** | **float** |  | [optional] 
**price_imperial_excl_tax** | **float** |  | [optional] 
**price_imperial_incl_tax** | **float** |  | [optional] 
**price_metric_excl_tax** | **float** |  | [optional] 
**price_metric_incl_tax** | **float** |  | [optional] 
**unit_price_texts** | [**List[SalesPriceUnitPriceUnitPriceTexts]**](SalesPriceUnitPriceUnitPriceTexts.md) |  | [optional] 
**display** | **bool** |  | 

## Example

```python
from salesitem_client.models.sales_price_unit_price import SalesPriceUnitPrice

# TODO update the JSON string below
json = "{}"
# create an instance of SalesPriceUnitPrice from a JSON string
sales_price_unit_price_instance = SalesPriceUnitPrice.from_json(json)
# print the JSON string representation of the object
print(SalesPriceUnitPrice.to_json())

# convert the object into a dict
sales_price_unit_price_dict = sales_price_unit_price_instance.to_dict()
# create an instance of SalesPriceUnitPrice from a dict
sales_price_unit_price_from_dict = SalesPriceUnitPrice.from_dict(sales_price_unit_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


