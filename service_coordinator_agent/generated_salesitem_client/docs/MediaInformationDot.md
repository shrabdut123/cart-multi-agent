# MediaInformationDot

Used for dots within images containing specific information on mouse hover, for example cut-through images. The coordinates specify where in the picture the given dot should be positioned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | [**MediaInformationDotCoordinates**](MediaInformationDotCoordinates.md) |  | [optional] 
**header** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.media_information_dot import MediaInformationDot

# TODO update the JSON string below
json = "{}"
# create an instance of MediaInformationDot from a JSON string
media_information_dot_instance = MediaInformationDot.from_json(json)
# print the JSON string representation of the object
print(MediaInformationDot.to_json())

# convert the object into a dict
media_information_dot_dict = media_information_dot_instance.to_dict()
# create an instance of MediaInformationDot from a dict
media_information_dot_from_dict = MediaInformationDot.from_dict(media_information_dot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


