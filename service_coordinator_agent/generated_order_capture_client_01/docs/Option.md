# Option

It refers to the option such as YES, NO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_value** | **str** | It describes an option YES, NO etc | 
**free_text_required** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.option import Option

# TODO update the JSON string below
json = "{}"
# create an instance of Option from a JSON string
option_instance = Option.from_json(json)
# print the JSON string representation of the object
print(Option.to_json())

# convert the object into a dict
option_dict = option_instance.to_dict()
# create an instance of Option from a dict
option_from_dict = Option.from_dict(option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


