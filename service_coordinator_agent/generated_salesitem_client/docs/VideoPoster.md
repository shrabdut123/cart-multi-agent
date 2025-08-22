# VideoPoster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_mime_type** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**quality** | **str** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from salesitem_client.models.video_poster import VideoPoster

# TODO update the JSON string below
json = "{}"
# create an instance of VideoPoster from a JSON string
video_poster_instance = VideoPoster.from_json(json)
# print the JSON string representation of the object
print(VideoPoster.to_json())

# convert the object into a dict
video_poster_dict = video_poster_instance.to_dict()
# create an instance of VideoPoster from a dict
video_poster_from_dict = VideoPoster.from_dict(video_poster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


