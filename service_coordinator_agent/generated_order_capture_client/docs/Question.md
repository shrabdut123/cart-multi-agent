# Question

List of questions for this type and delivery/service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | It refers to a question ID | [optional] 
**translated_reference** | **str** | It refers to a translated text of question ID | [optional] 
**options** | [**List[Option]**](Option.md) | It refers to the option such as YES, NO | [optional] 
**answer** | [**Answer**](Answer.md) |  | [optional] 
**regex** | **str** | It refers to a rule with which a free text is validated. It is not available for all free text questions. It depends on the type. Floor number is an example where it should be a number | [optional] 
**mandatory** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.question import Question

# TODO update the JSON string below
json = "{}"
# create an instance of Question from a JSON string
question_instance = Question.from_json(json)
# print the JSON string representation of the object
print(Question.to_json())

# convert the object into a dict
question_dict = question_instance.to_dict()
# create an instance of Question from a dict
question_from_dict = Question.from_dict(question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


