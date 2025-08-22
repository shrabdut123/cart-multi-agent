# BusinessUnit

Business Unit for the operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.business_unit import BusinessUnit

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessUnit from a JSON string
business_unit_instance = BusinessUnit.from_json(json)
# print the JSON string representation of the object
print(BusinessUnit.to_json())

# convert the object into a dict
business_unit_dict = business_unit_instance.to_dict()
# create an instance of BusinessUnit from a dict
business_unit_from_dict = BusinessUnit.from_dict(business_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


