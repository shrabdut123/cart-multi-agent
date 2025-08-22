# ConsumerInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the consumer | [optional] 
**checkout_type** | **str** | Type of checkout. It could be a checkout initiated from a regular web, a gift registry, business partner portal etc. | [optional] 
**return_url** | **str** | The URL where to land. Usually this is the URL of a client that initiated a  checkout so that the other clients that uses OC API shall send the customer back to the location of  initiation of checkout as part of error handling | [optional] 
**extra_info** | **Dict[str, str]** | Usually a pair of key values. These values are made available to other consumers if the request is handed over from one client to another client | [optional] 

## Example

```python
from order_capture_client.models.consumer_info_dto import ConsumerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerInfoDto from a JSON string
consumer_info_dto_instance = ConsumerInfoDto.from_json(json)
# print the JSON string representation of the object
print(ConsumerInfoDto.to_json())

# convert the object into a dict
consumer_info_dto_dict = consumer_info_dto_instance.to_dict()
# create an instance of ConsumerInfoDto from a dict
consumer_info_dto_from_dict = ConsumerInfoDto.from_dict(consumer_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


