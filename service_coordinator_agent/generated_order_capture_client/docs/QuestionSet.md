# QuestionSet

It describes the set of service questions for selected delivery service. The question set contains questions for different types of living

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | It refers to service item of a delivery or a service. It may contain comma separated value if the choice of delivery service has more than 1 delivery. It is deprecated and refer serviceIdServiceRelationMap | [optional] 
**service_method** | **str** | It refers to the method. It differs and it depends on whether it is delivery or a service.It may contain comma separated value if the choice of delivery service has more than 1 delivery. It is deprecated and refer serviceIdServiceRelationMap | [optional] 
**type** | **str** | It refers to the type of living i.e. HOUSE, FLAT etc | [optional] 
**questions** | [**List[Question]**](Question.md) | List of questions for this type and delivery/service | [optional] 
**service_id_service_relation_map** | [**Dict[str, ServiceQuestionRelation]**](ServiceQuestionRelation.md) | It contains a map of serviceId and service question relation. This map contains more than one key value if order is split into more than 1 delivery. It basically merges the question of same type of living | [optional] 

## Example

```python
from order_capture_client.models.question_set import QuestionSet

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionSet from a JSON string
question_set_instance = QuestionSet.from_json(json)
# print the JSON string representation of the object
print(QuestionSet.to_json())

# convert the object into a dict
question_set_dict = question_set_instance.to_dict()
# create an instance of QuestionSet from a dict
question_set_from_dict = QuestionSet.from_dict(question_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


