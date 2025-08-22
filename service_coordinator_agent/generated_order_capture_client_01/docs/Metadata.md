# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_price_recalculated** | **bool** | This parameter indicates if the selected delivery service and item prices are recalculated upon a patch call | [optional] 

## Example

```python
from order_capture_client.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


