# SlotPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incl_tax** | **float** |  | [optional] 
**excl_tax** | **float** |  | [optional] 

## Example

```python
from order_capture_client.models.slot_price import SlotPrice

# TODO update the JSON string below
json = "{}"
# create an instance of SlotPrice from a JSON string
slot_price_instance = SlotPrice.from_json(json)
# print the JSON string representation of the object
print(SlotPrice.to_json())

# convert the object into a dict
slot_price_dict = slot_price_instance.to_dict()
# create an instance of SlotPrice from a dict
slot_price_from_dict = SlotPrice.from_dict(slot_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


