# TWContextDto

It describes the context with which this request was operated on. This is an informational node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retail_unit** | **str** | Retail Unit code | [optional] 
**checkout_id** | **str** | Order capture generated UUID for a checkout | [optional] 
**delivery_arrangements_id** | **str** | iSOM provided identifier for delivery arrangement | [optional] 
**delivery_service_type** | **str** | It defines the delivery solution. HOME_DELIVERY has STANDARD, CURBSIDE, EXPRESS_CURBSIDE, EXPRESS, STANDARD_RD, CURBSIDE_RD, EXPRESS_CURBSIDE_RD, EXPRESS_RD. COLLECT has STANDARD and sometimes LOCKER for Internal lockers | [optional] 
**delivery_service_id** | **str** | Order capture generated UUID | [optional] 
**config** | [**TWConfigDto**](TWConfigDto.md) |  | [optional] 
**business_unit** | [**BusinessUnitDto**](BusinessUnitDto.md) |  | [optional] 
**customer_context** | [**CustomerContextDto**](CustomerContextDto.md) |  | [optional] 
**slot_based_pricing_enabled** | **bool** | It is true if slot based pricing is enabled | [optional] 

## Example

```python
from order_capture_client.models.tw_context_dto import TWContextDto

# TODO update the JSON string below
json = "{}"
# create an instance of TWContextDto from a JSON string
tw_context_dto_instance = TWContextDto.from_json(json)
# print the JSON string representation of the object
print(TWContextDto.to_json())

# convert the object into a dict
tw_context_dto_dict = tw_context_dto_instance.to_dict()
# create an instance of TWContextDto from a dict
tw_context_dto_from_dict = TWContextDto.from_dict(tw_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


