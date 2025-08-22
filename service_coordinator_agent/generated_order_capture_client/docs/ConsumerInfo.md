# ConsumerInfo

An object describing information about the consumer initiating the checkout (e.g CART, APP, CSS, iGift, ...etc), and what url should be a fallback in case of checkout errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**checkout_type** | **str** |  | [optional] 
**return_url** | **str** |  | [optional] 
**extra_info** | **Dict[str, str]** |  | [optional] 

## Example

```python
from order_capture_client.models.consumer_info import ConsumerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerInfo from a JSON string
consumer_info_instance = ConsumerInfo.from_json(json)
# print the JSON string representation of the object
print(ConsumerInfo.to_json())

# convert the object into a dict
consumer_info_dict = consumer_info_instance.to_dict()
# create an instance of ConsumerInfo from a dict
consumer_info_from_dict = ConsumerInfo.from_dict(consumer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


