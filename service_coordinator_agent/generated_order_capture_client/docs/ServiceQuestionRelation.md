# ServiceQuestionRelation

It contains a map of serviceId and service question relation. This map contains more than one key value if order is split into more than 1 delivery. It basically merges the question of same type of living

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_method** | **str** | It refers to a method of delivery i.e. TRUCK or PARCEL | [optional] 
**question_references** | **List[str]** | It refers to the list of question references for the associated serviceId | [optional] 

## Example

```python
from order_capture_client.models.service_question_relation import ServiceQuestionRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuestionRelation from a JSON string
service_question_relation_instance = ServiceQuestionRelation.from_json(json)
# print the JSON string representation of the object
print(ServiceQuestionRelation.to_json())

# convert the object into a dict
service_question_relation_dict = service_question_relation_instance.to_dict()
# create an instance of ServiceQuestionRelation from a dict
service_question_relation_from_dict = ServiceQuestionRelation.from_dict(service_question_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


