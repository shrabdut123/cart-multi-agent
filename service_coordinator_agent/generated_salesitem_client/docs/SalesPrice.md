# SalesPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_reason** | **str** | Further information about the specific price. | [optional] 
**currency_code** | **str** | Currency code for the price values | [optional] 
**indicative_discount** | **float** | Indicative discount percentage for the &#x60;IKEAFamilySalesUnitPrice&#x60; price type and the &#x60;RegularSalesUnitPrice&#x60; price type with reason code &#x60;TimeRestrictedOffer&#x60; | [optional] 
**indicative_total_tax** | **float** |  | [optional] 
**lowest_previous_sales_price** | [**SalesPricePreviousSalesPrice**](SalesPricePreviousSalesPrice.md) |  | [optional] 
**previous_sales_price** | [**SalesPricePreviousSalesPrice**](SalesPricePreviousSalesPrice.md) |  | [optional] 
**price_excl_tax** | **float** |  | [optional] 
**price_incl_tax** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**unit_price** | [**SalesPriceUnitPrice**](SalesPriceUnitPrice.md) |  | [optional] 
**experimental_discount_amount** | **float** | The difference of priceInclTax between RegularSalesUnitPrice and IKEAFamilySalesUnitPrice or TimeRestrictedOffer. This is an experimental property and can be removed at any time. | [optional] 
**experimental_discount_percentage** | **float** | The percentage difference in &#x60;priceInclTax&#x60; between &#x60;RegularSalesUnitPrice&#x60; and &#x60;IKEAFamilySalesUnitPrice&#x60; or &#x60;TimeRestrictedOffer&#x60;. This property is experimental and may be removed without notice. | [optional] 
**valid_from_date** | **date** | this is available in case changeReason is either Competition, NewLowerPrice, Temporary, TimeRestrictedOffer. | [optional] 
**valid_to_date** | **date** | this is available in case changeReason is either Competition, NewLowerPrice, Temporary, TimeRestrictedOffer. | [optional] 

## Example

```python
from salesitem_client.models.sales_price import SalesPrice

# TODO update the JSON string below
json = "{}"
# create an instance of SalesPrice from a JSON string
sales_price_instance = SalesPrice.from_json(json)
# print the JSON string representation of the object
print(SalesPrice.to_json())

# convert the object into a dict
sales_price_dict = sales_price_instance.to_dict()
# create an instance of SalesPrice from a dict
sales_price_from_dict = SalesPrice.from_dict(sales_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


