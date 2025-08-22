# ClassFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**values** | [**List[ClassFilterValue]**](ClassFilterValue.md) |  | [optional] 

## Example

```python
from salesitem_client.models.class_filter import ClassFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ClassFilter from a JSON string
class_filter_instance = ClassFilter.from_json(json)
# print the JSON string representation of the object
print(ClassFilter.to_json())

# convert the object into a dict
class_filter_dict = class_filter_instance.to_dict()
# create an instance of ClassFilter from a dict
class_filter_from_dict = ClassFilter.from_dict(class_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


