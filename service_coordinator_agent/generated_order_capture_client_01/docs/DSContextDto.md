# DSContextDto

It describes the context with which the request was operated. Informational node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retail_unit** | **str** | Retail Unit code | [optional] 
**excl_tax_country** | **bool** | A boolean that describes if a country initial prices are exclusive tax i.e. US, CA | [optional] 
**checkout_id** | **str** | Order capture generated UUID for a checkout | [optional] 
**currency** | **str** | Currency code | [optional] 
**scope** | [**ScopeDto**](ScopeDto.md) |  | [optional] 
**config** | [**DSConfigDto**](DSConfigDto.md) |  | [optional] 
**business_unit** | [**BusinessUnitDto**](BusinessUnitDto.md) |  | [optional] 
**customer_context** | [**CustomerContextDto**](CustomerContextDto.md) |  | [optional] 
**capability** | [**CapabilityDto**](CapabilityDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.ds_context_dto import DSContextDto

# TODO update the JSON string below
json = "{}"
# create an instance of DSContextDto from a JSON string
ds_context_dto_instance = DSContextDto.from_json(json)
# print the JSON string representation of the object
print(DSContextDto.to_json())

# convert the object into a dict
ds_context_dto_dict = ds_context_dto_instance.to_dict()
# create an instance of DSContextDto from a dict
ds_context_dto_from_dict = DSContextDto.from_dict(ds_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


