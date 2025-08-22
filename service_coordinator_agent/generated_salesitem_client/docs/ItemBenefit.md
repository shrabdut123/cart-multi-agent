# ItemBenefit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_benefit import ItemBenefit

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBenefit from a JSON string
item_benefit_instance = ItemBenefit.from_json(json)
# print the JSON string representation of the object
print(ItemBenefit.to_json())

# convert the object into a dict
item_benefit_dict = item_benefit_instance.to_dict()
# create an instance of ItemBenefit from a dict
item_benefit_from_dict = ItemBenefit.from_dict(item_benefit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


