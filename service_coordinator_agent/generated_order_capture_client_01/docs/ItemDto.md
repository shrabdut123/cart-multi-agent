# ItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**item_no** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**line_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**quantity_type** | **str** |  | [optional] 
**uom** | **str** |  | [optional] 
**total_price** | [**Price**](Price.md) |  | [optional] 
**availability** | [**Availability**](Availability.md) |  | [optional] 
**fees** | [**List[Fee]**](Fee.md) |  | [optional] 
**supported_delivery_method** | **str** |  | [optional] 
**external_ref_id** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.item_dto import ItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemDto from a JSON string
item_dto_instance = ItemDto.from_json(json)
# print the JSON string representation of the object
print(ItemDto.to_json())

# convert the object into a dict
item_dto_dict = item_dto_instance.to_dict()
# create an instance of ItemDto from a dict
item_dto_from_dict = ItemDto.from_dict(item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


