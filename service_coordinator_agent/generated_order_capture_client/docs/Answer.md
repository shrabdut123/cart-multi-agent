# Answer

It is not relevant for GET. It is relevant for save request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_value** | **str** | It describes an option YES, NO etc | [optional] 
**free_text** | **str** | It describes the free text entered by customer | [optional] 

## Example

```python
from order_capture_client.models.answer import Answer

# TODO update the JSON string below
json = "{}"
# create an instance of Answer from a JSON string
answer_instance = Answer.from_json(json)
# print the JSON string representation of the object
print(Answer.to_json())

# convert the object into a dict
answer_dict = answer_instance.to_dict()
# create an instance of Answer from a dict
answer_from_dict = Answer.from_dict(answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


