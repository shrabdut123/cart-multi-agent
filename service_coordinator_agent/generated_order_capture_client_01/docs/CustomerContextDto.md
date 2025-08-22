# CustomerContextDto

Customer context describing type of customer and additional identifiers such as familyId

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_type** | **str** | It describes the type of customer | [optional] 
**family_id** | **str** | It describes the family card number of a customer if family customer | [optional] 
**employee_id** | **str** | Future use | [optional] 

## Example

```python
from order_capture_client.models.customer_context_dto import CustomerContextDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerContextDto from a JSON string
customer_context_dto_instance = CustomerContextDto.from_json(json)
# print the JSON string representation of the object
print(CustomerContextDto.to_json())

# convert the object into a dict
customer_context_dto_dict = customer_context_dto_instance.to_dict()
# create an instance of CustomerContextDto from a dict
customer_context_dto_from_dict = CustomerContextDto.from_dict(customer_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


