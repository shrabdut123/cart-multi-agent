# Advertisement

Details of advertisements on discounted item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | **str** | Discount Type in SDM | [optional] 
**linked_items** | [**List[ItemKey]**](ItemKey.md) | List of items linked to the advertisement. | [optional] 
**localised_communications** | [**List[AdvertisementLocalisedCommunications]**](AdvertisementLocalisedCommunications.md) |  | [optional] 
**valid_for_customers** | **List[str]** | Customers who are eligible to view the advertisement. | [optional] 
**valid_from** | **date** | Start date of the advertisement. | [optional] 
**valid_to** | **date** | End date of the advertisement. | [optional] 

## Example

```python
from salesitem_client.models.advertisement import Advertisement

# TODO update the JSON string below
json = "{}"
# create an instance of Advertisement from a JSON string
advertisement_instance = Advertisement.from_json(json)
# print the JSON string representation of the object
print(Advertisement.to_json())

# convert the object into a dict
advertisement_dict = advertisement_instance.to_dict()
# create an instance of Advertisement from a dict
advertisement_from_dict = Advertisement.from_dict(advertisement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


