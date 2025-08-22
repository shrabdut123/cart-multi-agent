# TWConfig

It describes the configuration with which this request was executed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_number_of_days** | **str** |  | [optional] 
**excl_tax_country** | **bool** |  | [optional] 
**enable_isom_with_kong_gw** | **bool** |  | [optional] 
**enable_service_price_with_kong_gw** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.tw_config import TWConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TWConfig from a JSON string
tw_config_instance = TWConfig.from_json(json)
# print the JSON string representation of the object
print(TWConfig.to_json())

# convert the object into a dict
tw_config_dict = tw_config_instance.to_dict()
# create an instance of TWConfig from a dict
tw_config_from_dict = TWConfig.from_dict(tw_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


