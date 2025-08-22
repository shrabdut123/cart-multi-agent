# ConsumerContextInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shopping_type** | **str** | Determines the type of the checkout, whether it is created ONLINE or from STORE  | [optional] 
**channel** | **str** | Determines whether the checkout is initiated from MOBILE_APP or WEBAPP | [optional] 
**shopping_app_platform** | **str** | This is for order creation analytics. This will be sent to Selling             order creation. IKEAAPP_ should be aligned with channel i.e.             MOBILEAPP. If not passed, it defaults to WEB_BROWSER | [optional] 
**checkout_id** | **str** |  | [optional] 
**consumer_info** | [**ConsumerInfoDto**](ConsumerInfoDto.md) |  | [optional] 
**created** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.consumer_context_info_dto import ConsumerContextInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerContextInfoDto from a JSON string
consumer_context_info_dto_instance = ConsumerContextInfoDto.from_json(json)
# print the JSON string representation of the object
print(ConsumerContextInfoDto.to_json())

# convert the object into a dict
consumer_context_info_dto_dict = consumer_context_info_dto_instance.to_dict()
# create an instance of ConsumerContextInfoDto from a dict
consumer_context_info_dto_from_dict = ConsumerContextInfoDto.from_dict(consumer_context_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


