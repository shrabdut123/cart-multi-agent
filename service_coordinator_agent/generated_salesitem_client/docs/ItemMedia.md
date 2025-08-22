# ItemMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**VideoAction**](VideoAction.md) |  | [optional] 
**alt_text** | **str** |  | [optional] 
**transcript** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**information_dots** | [**List[MediaInformationDot]**](MediaInformationDot.md) |  | [optional] 
**name** | **str** |  | [optional] 
**pe_no** | **str** |  | [optional] 
**poster** | [**List[VideoPoster]**](VideoPoster.md) | Only applicable for types &#x60;PRODUCT_ASSEMBLY_VIDEO&#x60;, &#x60;PRODUCT_FEATURE_VIDEO&#x60; and &#x60;PRODUCT_USAGE_VIDEO&#x60;. The image to be shown while the video is downloading, see the [documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) for the HTML &#x60;video&#x60; element. The list is sorted in ascending order with regards to image dimensions. | [optional] 
**snapshots** | [**List[VideoSnapshot]**](VideoSnapshot.md) | Only applicable for types &#x60;PRODUCT_ASSEMBLY_VIDEO&#x60;, &#x60;PRODUCT_FEATURE_VIDEO&#x60; and &#x60;PRODUCT_USAGE_VIDEO&#x60;. Still images from a video. The list is sorted in ascending order with regards to which frame, in seconds, that an image represents in the video. | [optional] 
**thumbnail** | [**VideoThumbnail**](VideoThumbnail.md) |  | [optional] 
**type_name** | **str** |  | [optional] 
**type_no** | **str** |  | [optional] 
**variants** | [**List[MediaVariant]**](MediaVariant.md) |  | [optional] 

## Example

```python
from salesitem_client.models.item_media import ItemMedia

# TODO update the JSON string below
json = "{}"
# create an instance of ItemMedia from a JSON string
item_media_instance = ItemMedia.from_json(json)
# print the JSON string representation of the object
print(ItemMedia.to_json())

# convert the object into a dict
item_media_dict = item_media_instance.to_dict()
# create an instance of ItemMedia from a dict
item_media_from_dict = ItemMedia.from_dict(item_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


