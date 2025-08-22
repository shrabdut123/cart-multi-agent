# BusinessUnitDto

Business Unit for the operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | It describes the business unit code. At times it is retail unit itself i.e. SE or at times it is a code 010 and it depends on type | [optional] 
**type** | **str** | It describes the type of business unit STO or RU | [optional] 

## Example

```python
from order_capture_client.models.business_unit_dto import BusinessUnitDto

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessUnitDto from a JSON string
business_unit_dto_instance = BusinessUnitDto.from_json(json)
# print the JSON string representation of the object
print(BusinessUnitDto.to_json())

# convert the object into a dict
business_unit_dto_dict = business_unit_dto_instance.to_dict()
# create an instance of BusinessUnitDto from a dict
business_unit_dto_from_dict = BusinessUnitDto.from_dict(business_unit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


