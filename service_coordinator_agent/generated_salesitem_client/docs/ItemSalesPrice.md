# ItemSalesPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertisements** | [**List[Advertisement]**](Advertisement.md) |  | [optional] 
**class_unit_key** | [**ClassUnitKey**](ClassUnitKey.md) |  | [optional] 
**currency_rank** | **List[str]** | Sorted list of currencies. In most cases it will only have one entry.  In the case that there are multiple entries, the order dictates the priority.  For example, the order that the currencies should be presented towards customers. Meaning that the first entry has the highest priority. | [optional] 
**fees** | [**List[Fee]**](Fee.md) |  | [optional] 
**is_unit_price_preferred** | **bool** |  | [optional] 
**item_key** | [**ItemKey**](ItemKey.md) |  | [optional] 
**price_attributes** | [**List[PriceAttribute]**](PriceAttribute.md) | Additional attributes that are used in the communication of sales price. Only to be used for specific purpose information meaning used only by some touchpoints or channels, used only in specific scenarios, used only in specific markets for legal reasons or as a short term exception that will be resolved in the next version. FreeOfFreight enum should only be used for STO requests and is only temporarily exposed for RU requests for testing purposes and could be removed in the future. | [optional] 
**price_unit** | [**PriceUnit**](PriceUnit.md) |  | [optional] 
**sales_prices** | [**List[SalesPrice]**](SalesPrice.md) |  | [optional] 
**service_prices** | [**List[ServicePrice]**](ServicePrice.md) |  | [optional] 
**update_date_time** | **datetime** |  | [optional] 

## Example

```python
from salesitem_client.models.item_sales_price import ItemSalesPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ItemSalesPrice from a JSON string
item_sales_price_instance = ItemSalesPrice.from_json(json)
# print the JSON string representation of the object
print(ItemSalesPrice.to_json())

# convert the object into a dict
item_sales_price_dict = item_sales_price_instance.to_dict()
# create an instance of ItemSalesPrice from a dict
item_sales_price_from_dict = ItemSalesPrice.from_dict(item_sales_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


