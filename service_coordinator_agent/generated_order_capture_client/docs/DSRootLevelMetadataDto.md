# DSRootLevelMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_at_least_one_solution_fulfill_entire_cart** | **bool** |  | [optional] 
**expiry_time** | **str** |  | [optional] 
**has_at_least_one_no_stock_delivery** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.ds_root_level_metadata_dto import DSRootLevelMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of DSRootLevelMetadataDto from a JSON string
ds_root_level_metadata_dto_instance = DSRootLevelMetadataDto.from_json(json)
# print the JSON string representation of the object
print(DSRootLevelMetadataDto.to_json())

# convert the object into a dict
ds_root_level_metadata_dto_dict = ds_root_level_metadata_dto_instance.to_dict()
# create an instance of DSRootLevelMetadataDto from a dict
ds_root_level_metadata_dto_from_dict = DSRootLevelMetadataDto.from_dict(ds_root_level_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


