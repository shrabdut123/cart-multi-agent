# RemovalServiceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_of_failure** | **str** |  | [optional] 
**is_service_available** | **bool** |  | [optional] 

## Example

```python
from order_capture_client.models.removal_service_metadata import RemovalServiceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RemovalServiceMetadata from a JSON string
removal_service_metadata_instance = RemovalServiceMetadata.from_json(json)
# print the JSON string representation of the object
print(RemovalServiceMetadata.to_json())

# convert the object into a dict
removal_service_metadata_dict = removal_service_metadata_instance.to_dict()
# create an instance of RemovalServiceMetadata from a dict
removal_service_metadata_from_dict = RemovalServiceMetadata.from_dict(removal_service_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


