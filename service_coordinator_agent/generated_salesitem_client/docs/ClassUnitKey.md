# ClassUnitKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_unit_code** | **str** | Class unit code (for example &#39;SE&#39; or &#39;445&#39;) | 
**class_unit_type** | **str** | Class unit type (Currently supported: STO,RU) | 

## Example

```python
from salesitem_client.models.class_unit_key import ClassUnitKey

# TODO update the JSON string below
json = "{}"
# create an instance of ClassUnitKey from a JSON string
class_unit_key_instance = ClassUnitKey.from_json(json)
# print the JSON string representation of the object
print(ClassUnitKey.to_json())

# convert the object into a dict
class_unit_key_dict = class_unit_key_instance.to_dict()
# create an instance of ClassUnitKey from a dict
class_unit_key_from_dict = ClassUnitKey.from_dict(class_unit_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


