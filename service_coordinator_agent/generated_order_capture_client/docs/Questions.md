# Questions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_question** | [**List[QuestionSet]**](QuestionSet.md) | It describes the set of delivery questions for selected delivery service. The question set contains questions for different types of living | [optional] 
**service_question** | [**List[QuestionSet]**](QuestionSet.md) | It describes the set of service questions for selected delivery service. The question set contains questions for different types of living | [optional] 

## Example

```python
from order_capture_client.models.questions import Questions

# TODO update the JSON string below
json = "{}"
# create an instance of Questions from a JSON string
questions_instance = Questions.from_json(json)
# print the JSON string representation of the object
print(Questions.to_json())

# convert the object into a dict
questions_dict = questions_instance.to_dict()
# create an instance of Questions from a dict
questions_from_dict = Questions.from_dict(questions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


