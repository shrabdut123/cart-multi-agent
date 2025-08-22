# ServicePrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_reason** | **str** | Further information about the specific price. | [optional] 
**currency_code** | **str** | Currency code for the price values | [optional] 
**indicative_total_tax** | **float** |  | [optional] 
**previous_sales_price** | [**ServicePricePreviousSalesPrice**](ServicePricePreviousSalesPrice.md) |  | [optional] 
**price_excl_tax** | **float** |  | [optional] 
**price_incl_tax** | **float** |  | [optional] 
**service_product_id** | **str** | The id of the service product as defined by the retailer (e.g. BASIC_KITCHEN_INSTALL). | [optional] 
**type** | **str** |  | [optional] 
**valid_from_date** | **date** |  | [optional] 
**valid_to_date** | **date** |  | [optional] 

## Example

```python
from salesitem_client.models.service_price import ServicePrice

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePrice from a JSON string
service_price_instance = ServicePrice.from_json(json)
# print the JSON string representation of the object
print(ServicePrice.to_json())

# convert the object into a dict
service_price_dict = service_price_instance.to_dict()
# create an instance of ServicePrice from a dict
service_price_from_dict = ServicePrice.from_dict(service_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


