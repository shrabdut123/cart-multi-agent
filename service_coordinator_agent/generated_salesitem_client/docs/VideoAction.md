# VideoAction

A video action image, which is taken a few seconds into a video where there is supposed to be some \"action\". Only applicable for types `PRODUCT_ASSEMBLY_VIDEO`, `PRODUCT_FEATURE_VIDEO` and `PRODUCT_USAGE_VIDEO`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_mime_type** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from salesitem_client.models.video_action import VideoAction

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAction from a JSON string
video_action_instance = VideoAction.from_json(json)
# print the JSON string representation of the object
print(VideoAction.to_json())

# convert the object into a dict
video_action_dict = video_action_instance.to_dict()
# create an instance of VideoAction from a dict
video_action_from_dict = VideoAction.from_dict(video_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


