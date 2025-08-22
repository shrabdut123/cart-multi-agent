# STWContextDto

It describes the contextual information with which the request was operated on. This is for information purpose

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retail_unit** | **str** | Retail Unit code | [optional] 
**checkout_id** | **str** | Order capture generated UUID for a checkout | [optional] 
**zip_code** | **str** | Customer service zip code i.e. delivery or assembly, installation etc if supported | [optional] 
**state_code** | **str** | Customer state code if available. It is available for few countries i.e. US, CA, AU | [optional] 
**business_unit** | [**BusinessUnit**](BusinessUnit.md) |  | [optional] 
**delivery_service_type** | **str** | It defines the delivery solution. HOME_DELIVERY has STANDARD, CURBSIDE, EXPRESS_CURBSIDE, EXPRESS, STANDARD_RD, CURBSIDE_RD, EXPRESS_CURBSIDE_RD, EXPRESS_RD. COLLECT has STANDARD and sometimes LOCKER for Internal lockers | [optional] 
**delivery_service_id** | **str** | Order capture generated UUID | [optional] 
**time_zone** | **str** | It describes the time zone | [optional] 
**config** | [**TWConfig**](TWConfig.md) |  | [optional] 

## Example

```python
from order_capture_client.models.stw_context_dto import STWContextDto

# TODO update the JSON string below
json = "{}"
# create an instance of STWContextDto from a JSON string
stw_context_dto_instance = STWContextDto.from_json(json)
# print the JSON string representation of the object
print(STWContextDto.to_json())

# convert the object into a dict
stw_context_dto_dict = stw_context_dto_instance.to_dict()
# create an instance of STWContextDto from a dict
stw_context_dto_from_dict = STWContextDto.from_dict(stw_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


