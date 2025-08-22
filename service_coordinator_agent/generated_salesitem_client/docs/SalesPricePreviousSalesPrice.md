# SalesPricePreviousSalesPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **bool** |  | 
**indicative_total_tax** | **float** |  | [optional] 
**price_excl_tax** | **float** |  | [optional] 
**price_incl_tax** | **float** |  | [optional] 
**unit_price** | [**SalesPriceUnitPrice**](SalesPriceUnitPrice.md) |  | [optional] 

## Example

```python
from salesitem_client.models.sales_price_previous_sales_price import SalesPricePreviousSalesPrice

# TODO update the JSON string below
json = "{}"
# create an instance of SalesPricePreviousSalesPrice from a JSON string
sales_price_previous_sales_price_instance = SalesPricePreviousSalesPrice.from_json(json)
# print the JSON string representation of the object
print(SalesPricePreviousSalesPrice.to_json())

# convert the object into a dict
sales_price_previous_sales_price_dict = sales_price_previous_sales_price_instance.to_dict()
# create an instance of SalesPricePreviousSalesPrice from a dict
sales_price_previous_sales_price_from_dict = SalesPricePreviousSalesPrice.from_dict(sales_price_previous_sales_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


