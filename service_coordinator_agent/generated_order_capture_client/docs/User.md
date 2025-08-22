# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**family_card_no** | **str** |  | [optional] 
**profile_type** | **str** |  | [optional] 
**billing_contact** | [**BillingContact**](BillingContact.md) |  | [optional] 
**shipping_contact** | [**ShippingContact**](ShippingContact.md) |  | [optional] 

## Example

```python
from order_capture_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


