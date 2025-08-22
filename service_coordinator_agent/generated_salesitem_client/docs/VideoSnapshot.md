# VideoSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_mime_type** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**frame** | **int** | The frame, in seconds, that this image represents in the video. | [optional] 
**height** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from salesitem_client.models.video_snapshot import VideoSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of VideoSnapshot from a JSON string
video_snapshot_instance = VideoSnapshot.from_json(json)
# print the JSON string representation of the object
print(VideoSnapshot.to_json())

# convert the object into a dict
video_snapshot_dict = video_snapshot_instance.to_dict()
# create an instance of VideoSnapshot from a dict
video_snapshot_from_dict = VideoSnapshot.from_dict(video_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


