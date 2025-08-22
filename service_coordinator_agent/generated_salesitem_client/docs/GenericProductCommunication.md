# GenericProductCommunication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_unit_key** | [**ClassUnitKey**](ClassUnitKey.md) |  | [optional] 
**generic_product_no** | **str** | The number of the &#x60;GenericProduct&#x60;. | [optional] 
**item_keys** | [**List[ItemKey]**](ItemKey.md) |  | [optional] 
**localised_communications** | [**List[GenericProductLocalised]**](GenericProductLocalised.md) |  | [optional] 
**update_date_time** | **datetime** |  | [optional] 

## Example

```python
from salesitem_client.models.generic_product_communication import GenericProductCommunication

# TODO update the JSON string below
json = "{}"
# create an instance of GenericProductCommunication from a JSON string
generic_product_communication_instance = GenericProductCommunication.from_json(json)
# print the JSON string representation of the object
print(GenericProductCommunication.to_json())

# convert the object into a dict
generic_product_communication_dict = generic_product_communication_instance.to_dict()
# create an instance of GenericProductCommunication from a dict
generic_product_communication_from_dict = GenericProductCommunication.from_dict(generic_product_communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


