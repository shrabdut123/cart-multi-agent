# TimeWindowMetadataDto

It describes time window metadata and this is an informational attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | This describes if the time window capacity is available. This is an informational attribute | [optional] 

## Example

```python
from order_capture_client.models.time_window_metadata_dto import TimeWindowMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimeWindowMetadataDto from a JSON string
time_window_metadata_dto_instance = TimeWindowMetadataDto.from_json(json)
# print the JSON string representation of the object
print(TimeWindowMetadataDto.to_json())

# convert the object into a dict
time_window_metadata_dto_dict = time_window_metadata_dto_instance.to_dict()
# create an instance of TimeWindowMetadataDto from a dict
time_window_metadata_dto_from_dict = TimeWindowMetadataDto.from_dict(time_window_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


