# QuestionsAndAnswers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_id** | **str** |  | 
**user_id** | **str** |  | 
**questions_and_answers** | [**Questions**](Questions.md) |  | [optional] 

## Example

```python
from order_capture_client.models.questions_and_answers import QuestionsAndAnswers

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionsAndAnswers from a JSON string
questions_and_answers_instance = QuestionsAndAnswers.from_json(json)
# print the JSON string representation of the object
print(QuestionsAndAnswers.to_json())

# convert the object into a dict
questions_and_answers_dict = questions_and_answers_instance.to_dict()
# create an instance of QuestionsAndAnswers from a dict
questions_and_answers_from_dict = QuestionsAndAnswers.from_dict(questions_and_answers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


