# STWSelectedDSDto

It describes the selected delivery service along with the last delivery time. The service time window is calculated based on thsi selected information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solution_id** | **str** | It describes the selected delivery service | [optional] 
**deliveries** | [**List[STWDeliveryDto]**](STWDeliveryDto.md) | The deliveries and time windows of a selected service | [optional] 

## Example

```python
from order_capture_client.models.stw_selected_ds_dto import STWSelectedDSDto

# TODO update the JSON string below
json = "{}"
# create an instance of STWSelectedDSDto from a JSON string
stw_selected_ds_dto_instance = STWSelectedDSDto.from_json(json)
# print the JSON string representation of the object
print(STWSelectedDSDto.to_json())

# convert the object into a dict
stw_selected_ds_dto_dict = stw_selected_ds_dto_instance.to_dict()
# create an instance of STWSelectedDSDto from a dict
stw_selected_ds_dto_from_dict = STWSelectedDSDto.from_dict(stw_selected_ds_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


