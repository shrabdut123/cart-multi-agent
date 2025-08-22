# SelectedServiceDto

It describes the active services and it's time windows. It should be provided if the are at least one active service in the checkout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_item_no** | **str** | It refers to the selected service id | 
**service_product_id** | **str** | It refers to the service product | 
**time_window_id** | **str** | It refers to the selected service time window id | 

## Example

```python
from order_capture_client.models.selected_service_dto import SelectedServiceDto

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedServiceDto from a JSON string
selected_service_dto_instance = SelectedServiceDto.from_json(json)
# print the JSON string representation of the object
print(SelectedServiceDto.to_json())

# convert the object into a dict
selected_service_dto_dict = selected_service_dto_instance.to_dict()
# create an instance of SelectedServiceDto from a dict
selected_service_dto_from_dict = SelectedServiceDto.from_dict(selected_service_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


