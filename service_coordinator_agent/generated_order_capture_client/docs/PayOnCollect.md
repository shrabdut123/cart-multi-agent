# PayOnCollect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.pay_on_collect import PayOnCollect

# TODO update the JSON string below
json = "{}"
# create an instance of PayOnCollect from a JSON string
pay_on_collect_instance = PayOnCollect.from_json(json)
# print the JSON string representation of the object
print(PayOnCollect.to_json())

# convert the object into a dict
pay_on_collect_dict = pay_on_collect_instance.to_dict()
# create an instance of PayOnCollect from a dict
pay_on_collect_from_dict = PayOnCollect.from_dict(pay_on_collect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


