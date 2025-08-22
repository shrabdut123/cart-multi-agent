# News

Deprecated - use productTags instead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_from** | **date** |  | [optional] 
**valid_to** | **date** |  | [optional] 
**value** | **bool** | Is the item considered news according to RPIM API | [optional] 

## Example

```python
from salesitem_client.models.news import News

# TODO update the JSON string below
json = "{}"
# create an instance of News from a JSON string
news_instance = News.from_json(json)
# print the JSON string representation of the object
print(News.to_json())

# convert the object into a dict
news_dict = news_instance.to_dict()
# create an instance of News from a dict
news_from_dict = News.from_dict(news_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


