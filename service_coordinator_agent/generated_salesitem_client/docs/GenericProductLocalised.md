# GenericProductLocalised


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**language_code** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**selection_criteria** | [**List[SelectionCriteria]**](SelectionCriteria.md) |  | [optional] 

## Example

```python
from salesitem_client.models.generic_product_localised import GenericProductLocalised

# TODO update the JSON string below
json = "{}"
# create an instance of GenericProductLocalised from a JSON string
generic_product_localised_instance = GenericProductLocalised.from_json(json)
# print the JSON string representation of the object
print(GenericProductLocalised.to_json())

# convert the object into a dict
generic_product_localised_dict = generic_product_localised_instance.to_dict()
# create an instance of GenericProductLocalised from a dict
generic_product_localised_from_dict = GenericProductLocalised.from_dict(generic_product_localised_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


