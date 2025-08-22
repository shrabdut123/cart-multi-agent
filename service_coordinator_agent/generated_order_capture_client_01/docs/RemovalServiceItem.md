# RemovalServiceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **str** |  | [optional] 
**service_item_no** | **str** |  | [optional] 
**service_product_id** | **str** |  | [optional] 
**price** | [**Price**](Price.md) |  | [optional] 
**provider** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**price_calculation_value** | **float** |  | [optional] 
**taxation_info** | **str** |  | [optional] 
**removal_service_metadata** | [**RemovalServiceMetadata**](RemovalServiceMetadata.md) |  | [optional] 
**pay_to_provider** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.removal_service_item import RemovalServiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalServiceItem from a JSON string
removal_service_item_instance = RemovalServiceItem.from_json(json)
# print the JSON string representation of the object
print(RemovalServiceItem.to_json())

# convert the object into a dict
removal_service_item_dict = removal_service_item_instance.to_dict()
# create an instance of RemovalServiceItem from a dict
removal_service_item_from_dict = RemovalServiceItem.from_dict(removal_service_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


