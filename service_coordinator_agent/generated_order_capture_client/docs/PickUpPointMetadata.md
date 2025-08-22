# PickUpPointMetadata

It describes pick up point metadata that has lot of informational attribute such as selectable info, price. This is for easier consumption to avoid traversal to look up information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_service_id** | **str** | Order capture generated delivery UUID where this pick up point is connected | [optional] 
**delivery_service_solution** | **str** | iSOM provided identifier for a delivery solution where this pick up point is connected | [optional] 
**delivery_service_fulfillment_method_type** | **str** | iSOM provided delivery service category i.e. HOME_DELIVERY for example | [optional] 
**delivery_service_fulfillment_possibility** | **str** | This describes whether it can fulfill complete cart, partial or cannot fulfill due to complete unavailability. FULL - All items are available, NONE - No items are available and this is only for CLICK_COLLECT_STORE as of now, PARTIAL - Few are available | [optional] 
**delivery_id** | **str** | Order capture generated delivery UUID where this pick up point is connected | [optional] 
**delivery_type** | **str** | iSOM provided delivery type | [optional] 
**selectable_info** | [**SelectableInfo**](SelectableInfo.md) |  | [optional] 

## Example

```python
from order_capture_client.models.pick_up_point_metadata import PickUpPointMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PickUpPointMetadata from a JSON string
pick_up_point_metadata_instance = PickUpPointMetadata.from_json(json)
# print the JSON string representation of the object
print(PickUpPointMetadata.to_json())

# convert the object into a dict
pick_up_point_metadata_dict = pick_up_point_metadata_instance.to_dict()
# create an instance of PickUpPointMetadata from a dict
pick_up_point_metadata_from_dict = PickUpPointMetadata.from_dict(pick_up_point_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


