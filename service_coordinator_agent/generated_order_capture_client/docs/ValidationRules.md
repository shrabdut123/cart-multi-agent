# ValidationRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_tax_code_validation_required** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.validation_rules import ValidationRules

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationRules from a JSON string
validation_rules_instance = ValidationRules.from_json(json)
# print the JSON string representation of the object
print(ValidationRules.to_json())

# convert the object into a dict
validation_rules_dict = validation_rules_instance.to_dict()
# create an instance of ValidationRules from a dict
validation_rules_from_dict = ValidationRules.from_dict(validation_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


