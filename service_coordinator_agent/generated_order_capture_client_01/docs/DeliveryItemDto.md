# DeliveryItemDto

It contains a list of item complex types that are part of the delivery. At times, the orders are split into more than 1 delivery. This node provides information about items that are grouped under each delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_no** | **str** | It describes the article number that is part of a delivery | [optional] 
**item_type** | **str** | Type of item. Always ART as fulfillment does not consider groups like SPR. The availability and delivery is always at child level if SPR | [optional] 
**quantity** | **float** | Quantity of items that are part of delivery | [optional] 
**ship_node** | **str** | It describes the fulfillment unit from where it is shipped | [optional] 
**parent_id** | **str** | It refers to the SPR parent if the article happens to be a child of a SPR | [optional] 

## Example

```python
from order_capture_client.models.delivery_item_dto import DeliveryItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryItemDto from a JSON string
delivery_item_dto_instance = DeliveryItemDto.from_json(json)
# print the JSON string representation of the object
print(DeliveryItemDto.to_json())

# convert the object into a dict
delivery_item_dto_dict = delivery_item_dto_instance.to_dict()
# create an instance of DeliveryItemDto from a dict
delivery_item_dto_from_dict = DeliveryItemDto.from_dict(delivery_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


