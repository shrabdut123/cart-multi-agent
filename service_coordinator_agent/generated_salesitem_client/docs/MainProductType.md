# MainProductType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Main Product Type (&#x60;MPT&#x60;), e.g., &#x60;SPR table + chair&#x60; or &#x60;wardrobes&#x60;. This field is always in English. | [optional] 
**var_false** | **str** | The unique identifier for the Main Product Type (&#x60;MPT&#x60;), e.g., &#x60;00038&#x60; and &#x60;00076&#x60;. | [optional] 

## Example

```python
from salesitem_client.models.main_product_type import MainProductType

# TODO update the JSON string below
json = "{}"
# create an instance of MainProductType from a JSON string
main_product_type_instance = MainProductType.from_json(json)
# print the JSON string representation of the object
print(MainProductType.to_json())

# convert the object into a dict
main_product_type_dict = main_product_type_instance.to_dict()
# create an instance of MainProductType from a dict
main_product_type_from_dict = MainProductType.from_dict(main_product_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


