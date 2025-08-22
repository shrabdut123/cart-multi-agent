# ItemAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_attachment import ItemAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAttachment from a JSON string
item_attachment_instance = ItemAttachment.from_json(json)
# print the JSON string representation of the object
print(ItemAttachment.to_json())

# convert the object into a dict
item_attachment_dict = item_attachment_instance.to_dict()
# create an instance of ItemAttachment from a dict
item_attachment_from_dict = ItemAttachment.from_dict(item_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


