# CheckoutExpiryMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_timestamp** | **str** |  | [optional] 
**time_left_to_expire_in_sec** | **int** |  | [optional] 

## Example

```python
from order_capture_client.models.checkout_expiry_metadata import CheckoutExpiryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutExpiryMetadata from a JSON string
checkout_expiry_metadata_instance = CheckoutExpiryMetadata.from_json(json)
# print the JSON string representation of the object
print(CheckoutExpiryMetadata.to_json())

# convert the object into a dict
checkout_expiry_metadata_dict = checkout_expiry_metadata_instance.to_dict()
# create an instance of CheckoutExpiryMetadata from a dict
checkout_expiry_metadata_from_dict = CheckoutExpiryMetadata.from_dict(checkout_expiry_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


