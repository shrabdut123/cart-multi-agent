# SpeAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_type** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 

## Example

```python
from order_capture_client.models.spe_amount import SpeAmount

# TODO update the JSON string below
json = "{}"
# create an instance of SpeAmount from a JSON string
spe_amount_instance = SpeAmount.from_json(json)
# print the JSON string representation of the object
print(SpeAmount.to_json())

# convert the object into a dict
spe_amount_dict = spe_amount_instance.to_dict()
# create an instance of SpeAmount from a dict
spe_amount_from_dict = SpeAmount.from_dict(spe_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


