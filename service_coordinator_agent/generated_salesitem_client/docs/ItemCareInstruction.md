# ItemCareInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**care_instruction_header** | **str** |  | [optional] 
**care_instruction_texts** | [**List[CareInstructionText]**](CareInstructionText.md) |  | [optional] 
**product_type_text** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_care_instruction import ItemCareInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCareInstruction from a JSON string
item_care_instruction_instance = ItemCareInstruction.from_json(json)
# print the JSON string representation of the object
print(ItemCareInstruction.to_json())

# convert the object into a dict
item_care_instruction_dict = item_care_instruction_instance.to_dict()
# create an instance of ItemCareInstruction from a dict
item_care_instruction_from_dict = ItemCareInstruction.from_dict(item_care_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


