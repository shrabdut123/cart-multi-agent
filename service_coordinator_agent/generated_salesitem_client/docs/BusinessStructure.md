# BusinessStructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_furnishing_business_name** | **str** |  | [optional] 
**home_furnishing_business_no** | **str** |  | [optional] 
**product_area_name** | **str** |  | [optional] 
**product_area_no** | **str** |  | [optional] 
**product_range_area_name** | **str** |  | [optional] 
**product_range_area_no** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.business_structure import BusinessStructure

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessStructure from a JSON string
business_structure_instance = BusinessStructure.from_json(json)
# print the JSON string representation of the object
print(BusinessStructure.to_json())

# convert the object into a dict
business_structure_dict = business_structure_instance.to_dict()
# create an instance of BusinessStructure from a dict
business_structure_from_dict = BusinessStructure.from_dict(business_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


