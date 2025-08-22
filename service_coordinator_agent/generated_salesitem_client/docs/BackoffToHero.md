# BackoffToHero


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**heroes** | [**List[ItemHero]**](ItemHero.md) |  | [optional] 

## Example

```python
from salesitem_client.models.backoff_to_hero import BackoffToHero

# TODO update the JSON string below
json = "{}"
# create an instance of BackoffToHero from a JSON string
backoff_to_hero_instance = BackoffToHero.from_json(json)
# print the JSON string representation of the object
print(BackoffToHero.to_json())

# convert the object into a dict
backoff_to_hero_dict = backoff_to_hero_instance.to_dict()
# create an instance of BackoffToHero from a dict
backoff_to_hero_from_dict = BackoffToHero.from_dict(backoff_to_hero_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


