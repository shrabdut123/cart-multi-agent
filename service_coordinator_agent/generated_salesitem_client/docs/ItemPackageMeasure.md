# ItemPackageMeasure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack_no** | **int** |  | [optional] 
**text_imperial** | **str** |  | [optional] 
**text_metric** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**type_name** | **str** |  | [optional] 
**unit_imperial** | **str** |  | [optional] 
**unit_metric** | **str** |  | [optional] 
**value_imperial** | **str** |  | [optional] 
**value_metric** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.item_package_measure import ItemPackageMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPackageMeasure from a JSON string
item_package_measure_instance = ItemPackageMeasure.from_json(json)
# print the JSON string representation of the object
print(ItemPackageMeasure.to_json())

# convert the object into a dict
item_package_measure_dict = item_package_measure_instance.to_dict()
# create an instance of ItemPackageMeasure from a dict
item_package_measure_from_dict = ItemPackageMeasure.from_dict(item_package_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


