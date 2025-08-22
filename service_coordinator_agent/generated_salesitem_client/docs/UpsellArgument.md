# UpsellArgument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_text** | **str** |  | [optional] 
**short_text** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.upsell_argument import UpsellArgument

# TODO update the JSON string below
json = "{}"
# create an instance of UpsellArgument from a JSON string
upsell_argument_instance = UpsellArgument.from_json(json)
# print the JSON string representation of the object
print(UpsellArgument.to_json())

# convert the object into a dict
upsell_argument_dict = upsell_argument_instance.to_dict()
# create an instance of UpsellArgument from a dict
upsell_argument_from_dict = UpsellArgument.from_dict(upsell_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


