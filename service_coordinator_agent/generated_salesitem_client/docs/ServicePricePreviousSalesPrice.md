# ServicePricePreviousSalesPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indicative_total_tax** | **float** |  | [optional] 
**price_excl_tax** | **float** |  | [optional] 
**price_incl_tax** | **float** |  | [optional] 

## Example

```python
from salesitem_client.models.service_price_previous_sales_price import ServicePricePreviousSalesPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePricePreviousSalesPrice from a JSON string
service_price_previous_sales_price_instance = ServicePricePreviousSalesPrice.from_json(json)
# print the JSON string representation of the object
print(ServicePricePreviousSalesPrice.to_json())

# convert the object into a dict
service_price_previous_sales_price_dict = service_price_previous_sales_price_instance.to_dict()
# create an instance of ServicePricePreviousSalesPrice from a dict
service_price_previous_sales_price_from_dict = ServicePricePreviousSalesPrice.from_dict(service_price_previous_sales_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


