# PickUpPointEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oc_pupid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**lsc** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**opening_hours_mon_time** | **str** |  | [optional] 
**opening_hours_tue_time** | **str** |  | [optional] 
**opening_hours_wed_time** | **str** |  | [optional] 
**opening_hours_thu_time** | **str** |  | [optional] 
**opening_hours_fri_time** | **str** |  | [optional] 
**opening_hours_sat_time** | **str** |  | [optional] 
**opening_hours_sun_time** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**address_line4** | **str** |  | [optional] 
**distance** | **float** |  | [optional] 

## Example

```python
from order_capture_client.models.pick_up_point_entity import PickUpPointEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PickUpPointEntity from a JSON string
pick_up_point_entity_instance = PickUpPointEntity.from_json(json)
# print the JSON string representation of the object
print(PickUpPointEntity.to_json())

# convert the object into a dict
pick_up_point_entity_dict = pick_up_point_entity_instance.to_dict()
# create an instance of PickUpPointEntity from a dict
pick_up_point_entity_from_dict = PickUpPointEntity.from_dict(pick_up_point_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


