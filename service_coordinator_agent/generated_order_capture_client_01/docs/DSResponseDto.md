# DSResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**DSContextDto**](DSContextDto.md) |  | [optional] 
**error** | [**ErrorDto**](ErrorDto.md) |  | [optional] 
**possible_delivery_services** | [**PossibleDeliveryServicesDto**](PossibleDeliveryServicesDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.ds_response_dto import DSResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DSResponseDto from a JSON string
ds_response_dto_instance = DSResponseDto.from_json(json)
# print the JSON string representation of the object
print(DSResponseDto.to_json())

# convert the object into a dict
ds_response_dto_dict = ds_response_dto_instance.to_dict()
# create an instance of DSResponseDto from a dict
ds_response_dto_from_dict = DSResponseDto.from_dict(ds_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


