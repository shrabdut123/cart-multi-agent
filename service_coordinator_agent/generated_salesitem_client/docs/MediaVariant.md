# MediaVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_mime_type** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**href** | **str** | An SEO friendly URL having the format &#x60;https://www.ikea.com/{countryCode}/{languageCode}/images/products/{productName}-{productType}-{validDesignText}__{fileName}.JPG&#x60;. If &#x60;productName&#x60; and/or &#x60;productType&#x60; don&#39;t exist, then the original URL is returned. If &#x60;validDesignText&#x60; doesn&#39;t exist, then it is simply omitted from the URL. | [optional] 
**quality** | **str** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from salesitem_client.models.media_variant import MediaVariant

# TODO update the JSON string below
json = "{}"
# create an instance of MediaVariant from a JSON string
media_variant_instance = MediaVariant.from_json(json)
# print the JSON string representation of the object
print(MediaVariant.to_json())

# convert the object into a dict
media_variant_dict = media_variant_instance.to_dict()
# create an instance of MediaVariant from a dict
media_variant_from_dict = MediaVariant.from_dict(media_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


