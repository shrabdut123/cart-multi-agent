# PickUpPointDto

List of possible pick up points with details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oc_pupid** | **str** | It describes the order capture generated UUID for a pick up point. Consumer must use this in API | [optional] 
**sto** | **str** | This information is only available for collect at store pick up points. This is subject to change in the future. | [optional] 
**metadata** | [**PickUpPointMetadata**](PickUpPointMetadata.md) |  | [optional] 
**price** | [**PUPPrice**](PUPPrice.md) |  | [optional] 
**id** | **str** | iSOM provided ID for a pick up point | [optional] 
**name** | **str** | iSOM provided name for a pick up point | [optional] 
**identifier** | **str** | iSOM provided identifier for a pick up point | [optional] 
**lsc** | **str** | iSOM provided merge node | [optional] 
**latitude** | **str** | iSOM provided co-ordinates i.e. latitude and longitude | [optional] 
**longitude** | **str** | iSOM provided co-ordinates i.e. latitude and longitude | [optional] 
**opening_hours_mon_time** | **str** | iSOM provided opening hours for each day. May included comma separated time range if collection point has more than 1 range of opening hours within a day | [optional] 
**opening_hours_tue_time** | **str** | iSOM provided opening hours for each day. May included comma separated time range if collection point has more than 1 range of opening hours within a day | [optional] 
**opening_hours_wed_time** | **str** | iSOM provided opening hours for each day. May included comma separated time range if collection point has more than 1 range of opening hours within a day | [optional] 
**opening_hours_thu_time** | **str** | iSOM provided opening hours for each day. May included comma separated time range if collection point has more than 1 range of opening hours within a day | [optional] 
**opening_hours_fri_time** | **str** | iSOM provided opening hours for each day. May included comma separated time range if collection point has more than 1 range of opening hours within a day | [optional] 
**opening_hours_sat_time** | **str** | iSOM provided opening hours for each day. May included comma separated time range if collection point has more than 1 range of opening hours within a day | [optional] 
**opening_hours_sun_time** | **str** | iSOM provided opening hours for each day. May included comma separated time range if collection point has more than 1 range of opening hours within a day | [optional] 
**country** | **str** | iSOM provided Country Code | [optional] 
**zip_code** | **str** | iSOM provided Zipcode | [optional] 
**city** | **str** | iSOM provided City | [optional] 
**state** | **str** | iSOM provided State Code. It may not be available always and it depends on the country | [optional] 
**address_line1** | **str** | iSOM provided Address lines | [optional] 
**address_line2** | **str** | iSOM provided Address lines | [optional] 
**address_line3** | **str** | iSOM provided Address lines | [optional] 
**address_line4** | **str** | iSOM provided Address lines | [optional] 
**distance** | **float** | iSOM provided Distance to customer zip code | [optional] 
**time_windows** | [**TimeWindowsDto**](TimeWindowsDto.md) |  | [optional] 

## Example

```python
from order_capture_client.models.pick_up_point_dto import PickUpPointDto

# TODO update the JSON string below
json = "{}"
# create an instance of PickUpPointDto from a JSON string
pick_up_point_dto_instance = PickUpPointDto.from_json(json)
# print the JSON string representation of the object
print(PickUpPointDto.to_json())

# convert the object into a dict
pick_up_point_dto_dict = pick_up_point_dto_instance.to_dict()
# create an instance of PickUpPointDto from a dict
pick_up_point_dto_from_dict = PickUpPointDto.from_dict(pick_up_point_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


