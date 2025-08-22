# ItemAvailabilityClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_classifications** | [**List[AvailabilityClassification]**](AvailabilityClassification.md) |  | [optional] 
**class_unit_key** | [**ClassUnitKey**](ClassUnitKey.md) |  | [optional] 
**item_key** | [**ItemKey**](ItemKey.md) |  | [optional] 
**update_date_time** | **datetime** |  | [optional] 

## Example

```python
from salesitem_client.models.item_availability_classification import ItemAvailabilityClassification

# TODO update the JSON string below
json = "{}"
# create an instance of ItemAvailabilityClassification from a JSON string
item_availability_classification_instance = ItemAvailabilityClassification.from_json(json)
# print the JSON string representation of the object
print(ItemAvailabilityClassification.to_json())

# convert the object into a dict
item_availability_classification_dict = item_availability_classification_instance.to_dict()
# create an instance of ItemAvailabilityClassification from a dict
item_availability_classification_from_dict = ItemAvailabilityClassification.from_dict(item_availability_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


