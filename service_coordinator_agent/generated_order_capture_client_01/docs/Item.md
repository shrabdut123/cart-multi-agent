# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**item_no** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**line_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 
**quantity_type** | **str** |  | [optional] 
**total_price** | [**Price**](Price.md) |  | [optional] 
**availability** | [**Availability**](Availability.md) |  | [optional] 
**child_items** | [**List[Item]**](Item.md) |  | [optional] 
**fees** | [**List[Fee]**](Fee.md) |  | [optional] 
**uom** | **str** |  | [optional] 
**supported_delivery_method** | **str** |  | [optional] 
**taxation_info** | **str** | Taxation Info value sent by SPE as encoded | [optional] 
**group** | **str** |  | [optional] 
**shopping_profile** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


