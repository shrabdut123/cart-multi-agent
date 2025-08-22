# CertificationMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_text** | **str** | Alternate text for image | [optional] 
**display_text** | **str** | Text to be displayed instead of image when space is limited | [optional] 
**media_info_url** | **str** | Link to test institutes website for additional information | [optional] 
**type** | **str** |  | [optional] 
**variants** | [**List[MediaVariant]**](MediaVariant.md) |  | [optional] 

## Example

```python
from salesitem_client.models.certification_media import CertificationMedia

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationMedia from a JSON string
certification_media_instance = CertificationMedia.from_json(json)
# print the JSON string representation of the object
print(CertificationMedia.to_json())

# convert the object into a dict
certification_media_dict = certification_media_instance.to_dict()
# create an instance of CertificationMedia from a dict
certification_media_from_dict = CertificationMedia.from_dict(certification_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


