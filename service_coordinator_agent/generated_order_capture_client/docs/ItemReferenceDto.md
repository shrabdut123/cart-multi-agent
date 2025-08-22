# ItemReferenceDto

It refers to the items for which the service is requested

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_no** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.item_reference_dto import ItemReferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemReferenceDto from a JSON string
item_reference_dto_instance = ItemReferenceDto.from_json(json)
# print the JSON string representation of the object
print(ItemReferenceDto.to_json())

# convert the object into a dict
item_reference_dto_dict = item_reference_dto_instance.to_dict()
# create an instance of ItemReferenceDto from a dict
item_reference_dto_from_dict = ItemReferenceDto.from_dict(item_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


