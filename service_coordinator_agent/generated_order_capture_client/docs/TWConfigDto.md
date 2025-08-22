# TWConfigDto

It describes the configuration with which this request was executed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_number_of_days** | **str** | It describes the scope of the search. It is basically the earliest possible date plus the number of days. The available slots within this will be returned | [optional] 
**excl_tax_country** | **bool** | It describes if the initial country price is exclusive tax i.e. US, CA | [optional] 

## Example

```python
from order_capture_client.models.tw_config_dto import TWConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of TWConfigDto from a JSON string
tw_config_dto_instance = TWConfigDto.from_json(json)
# print the JSON string representation of the object
print(TWConfigDto.to_json())

# convert the object into a dict
tw_config_dto_dict = tw_config_dto_instance.to_dict()
# create an instance of TWConfigDto from a dict
tw_config_dto_from_dict = TWConfigDto.from_dict(tw_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


