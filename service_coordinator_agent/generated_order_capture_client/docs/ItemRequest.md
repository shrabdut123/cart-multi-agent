# ItemRequest

List of items added to the cart and ready for checkout, Each item line should be unique and must not repeat. If there are 2             lines with same article number, it should be sent as one line with             sum of both quantity lines. The availability of the article line             must be verified before passing in

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_no** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**uom** | **str** | Unit Of Measurement, e.g. PIECE, METER | [optional] 
**group** | **str** |  | [optional] 
**shopping_profile** | **str** |  | [optional] 
**external_ref_id** | **str** | Only required for order-modification scenarios (e.g no-stock orders) | [optional] 

## Example

```python
from order_capture_client.models.item_request import ItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ItemRequest from a JSON string
item_request_instance = ItemRequest.from_json(json)
# print the JSON string representation of the object
print(ItemRequest.to_json())

# convert the object into a dict
item_request_dict = item_request_instance.to_dict()
# create an instance of ItemRequest from a dict
item_request_from_dict = ItemRequest.from_dict(item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


