# AdvertisementLocalisedCommunications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**full** | **str** | Full advertisement text | [optional] 
**language_code** | **str** |  | [optional] 
**short** | **str** | Short advertisement text | [optional] 

## Example

```python
from salesitem_client.models.advertisement_localised_communications import AdvertisementLocalisedCommunications

# TODO update the JSON string below
json = "{}"
# create an instance of AdvertisementLocalisedCommunications from a JSON string
advertisement_localised_communications_instance = AdvertisementLocalisedCommunications.from_json(json)
# print the JSON string representation of the object
print(AdvertisementLocalisedCommunications.to_json())

# convert the object into a dict
advertisement_localised_communications_dict = advertisement_localised_communications_instance.to_dict()
# create an instance of AdvertisementLocalisedCommunications from a dict
advertisement_localised_communications_from_dict = AdvertisementLocalisedCommunications.from_dict(advertisement_localised_communications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


