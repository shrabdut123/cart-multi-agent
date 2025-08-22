# DSMetadataDto

It describes the delivery service metadata which includes information about delivery choice selection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectable_info** | [**SelectableInfo**](SelectableInfo.md) |  | [optional] 
**service_offer_compatible** | **bool** | It describes whether this delivery can be combined for assembly service online. This is used to query service time window for assembly services. This attribute is relevant only for markets that are selling services online | [optional] 
**assembly_service_compatible** | **bool** | It describes whether this delivery can be combined for assembly service online. This is used to query service time window for assembly services. This attribute is relevant only for markets that are selling services online | [optional] 
**removal_sofa_compatible** | **bool** | It describes whether the selected removal service is compatible with this delivery. This is used to query service time window for removal services. This attribute is relevant only for markets that are selling removal services online | [optional] 
**removal_mattress_compatible** | **bool** | It describes whether the selected removal service is compatible with this delivery. This is used to query service time window for removal services. This attribute is relevant only for markets that are selling removal services online | [optional] 
**removal_white_goods_compatible** | **bool** | It describes whether the selected removal service is compatible with this delivery. This is used to query service time window for removal services. This attribute is relevant only for markets that are selling removal services online | [optional] 
**wheel_chair_capability** | **bool** | It describes whether the delivery service supports collecting a consent for keeping the goods in lower compartment. Usually applies for locker as customer does self pick up from a locker compartment | [optional] 
**slot_based_pricing_enabled** | **bool** | It describes whether each time window has different pricing. It is relevant if the market has prime time pricing enabled | [optional] 
**max_solution_price** | **float** | It describes the maximum possible solution price in case of a PUP solution | [optional] 
**min_solution_price** | **float** | It describes the minimum possible solution price in case of a PUP solution | [optional] 
**delivery_price_based_on_pup_zip_code** | **bool** | It describes whether the PUP Zipcode based price calculation is used or not | [optional] 
**has_no_stock_delivery** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.ds_metadata_dto import DSMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DSMetadataDto from a JSON string
ds_metadata_dto_instance = DSMetadataDto.from_json(json)
# print the JSON string representation of the object
print(DSMetadataDto.to_json())

# convert the object into a dict
ds_metadata_dto_dict = ds_metadata_dto_instance.to_dict()
# create an instance of DSMetadataDto from a dict
ds_metadata_dto_from_dict = DSMetadataDto.from_dict(ds_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


