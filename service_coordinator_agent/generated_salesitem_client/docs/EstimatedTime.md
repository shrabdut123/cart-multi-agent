# EstimatedTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from salesitem_client.models.estimated_time import EstimatedTime

# TODO update the JSON string below
json = "{}"
# create an instance of EstimatedTime from a JSON string
estimated_time_instance = EstimatedTime.from_json(json)
# print the JSON string representation of the object
print(EstimatedTime.to_json())

# convert the object into a dict
estimated_time_dict = estimated_time_instance.to_dict()
# create an instance of EstimatedTime from a dict
estimated_time_from_dict = EstimatedTime.from_dict(estimated_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


