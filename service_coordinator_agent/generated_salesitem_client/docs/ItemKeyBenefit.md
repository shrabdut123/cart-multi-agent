# ItemKeyBenefit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heading_text** | **str** |  | 
**text** | **str** |  | 
**type** | **str** |  | 
**unit_of_measure** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_key_benefit import ItemKeyBenefit

# TODO update the JSON string below
json = "{}"
# create an instance of ItemKeyBenefit from a JSON string
item_key_benefit_instance = ItemKeyBenefit.from_json(json)
# print the JSON string representation of the object
print(ItemKeyBenefit.to_json())

# convert the object into a dict
item_key_benefit_dict = item_key_benefit_instance.to_dict()
# create an instance of ItemKeyBenefit from a dict
item_key_benefit_from_dict = ItemKeyBenefit.from_dict(item_key_benefit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


