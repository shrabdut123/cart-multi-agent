# ServiceProductRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hide_service_from_customer** | **bool** | Defines if the service is hidden from customers or not. Service that is not visible is only bookable by Coworker systems. | [optional] 
**is_co_worker_assistance_needed** | **bool** | Defines if there is a need for co-worker interaction or if the service product can be bought without co-worker involvement. | [optional] 
**is_promoted** | **bool** | Defines if the related service product should be used in communication of the physical product (e.g. on product views such as PIP). | [optional] 
**recommendation_rank** | **int** | Defines the order of importance compared with other related service products in communication with customers (e.g. on a product view such as PIP). | [optional] 
**relation_type** | **str** | Describes the type of relation e.g. if is bought together with, are related to etc. | [optional] 
**service_key** | [**ItemKey**](ItemKey.md) |  | [optional] 
**service_product_id** | **str** | The id of the service product as defined by the retailer (e.g. BASIC_KITCHEN_INSTALL). | [optional] 
**service_product_type** | **str** | Defines the type of service used in communication towards customers (e.g. sofa assembly and furniture assembly are both communicated as assembly). | [optional] 

## Example

```python
from salesitem_client.models.service_product_relation import ServiceProductRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProductRelation from a JSON string
service_product_relation_instance = ServiceProductRelation.from_json(json)
# print the JSON string representation of the object
print(ServiceProductRelation.to_json())

# convert the object into a dict
service_product_relation_dict = service_product_relation_instance.to_dict()
# create an instance of ServiceProductRelation from a dict
service_product_relation_from_dict = ServiceProductRelation.from_dict(service_product_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


