# UnavailableItemDto

It contains a list of unavailable items for a delivery service with a reason of unavailability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order capture generated UUID for an item. It is the same as checkout items UUID | [optional] 
**line_id** | **str** | It is a unique identifier used for external interactions i.e. towards iSOM, iServe. Consumers should NOT use this for reference | [optional] 
**item_no** | **str** | It describes the article number | [optional] 
**type** | **str** | It describes the type of the item ART or SPR | [optional] 
**required_quantity** | **float** | It describes the quantity ordered by customer | [optional] 
**available_quantity** | **float** | It describes the available quantity. It is possible either all are unavailable or part of the quantity are unavailable | [optional] 
**unavailable_reason** | **str** | It describes the reason of unavailability. The unavailable reason are directly from iSOM | [optional] 
**unavailable_reason_code_map** | **Dict[str, str]** | At times there are more than one unavailable reason. This is possible if the type is SPR and each child of SPR can have its own unavailable reason. It is also possible if the ordered quantity is higher. The map has article number in key and reason as a value  | [optional] 

## Example

```python
from order_capture_client.models.unavailable_item_dto import UnavailableItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnavailableItemDto from a JSON string
unavailable_item_dto_instance = UnavailableItemDto.from_json(json)
# print the JSON string representation of the object
print(UnavailableItemDto.to_json())

# convert the object into a dict
unavailable_item_dto_dict = unavailable_item_dto_instance.to_dict()
# create an instance of UnavailableItemDto from a dict
unavailable_item_dto_from_dict = UnavailableItemDto.from_dict(unavailable_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


