# ServiceOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**service_price** | [**Price**](Price.md) |  | [optional] 
**inactive_reason** | **str** |  | [optional] 
**service_product_id** | **str** |  | [optional] 
**service_item_number** | **str** |  | [optional] 
**market_csc_enabled** | **bool** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.service_offer import ServiceOffer

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceOffer from a JSON string
service_offer_instance = ServiceOffer.from_json(json)
# print the JSON string representation of the object
print(ServiceOffer.to_json())

# convert the object into a dict
service_offer_dict = service_offer_instance.to_dict()
# create an instance of ServiceOffer from a dict
service_offer_from_dict = ServiceOffer.from_dict(service_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


