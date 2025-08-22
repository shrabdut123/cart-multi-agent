# ForecastGet200ResponseCurrentWeatherUnits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**temperature** | **str** |  | [optional] 
**windspeed** | **str** |  | [optional] 
**winddirection** | **str** |  | [optional] 
**is_day** | **str** |  | [optional] 
**weathercode** | **str** |  | [optional] 

## Example

```python
from weather_client.models.forecast_get200_response_current_weather_units import ForecastGet200ResponseCurrentWeatherUnits

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastGet200ResponseCurrentWeatherUnits from a JSON string
forecast_get200_response_current_weather_units_instance = ForecastGet200ResponseCurrentWeatherUnits.from_json(json)
# print the JSON string representation of the object
print(ForecastGet200ResponseCurrentWeatherUnits.to_json())

# convert the object into a dict
forecast_get200_response_current_weather_units_dict = forecast_get200_response_current_weather_units_instance.to_dict()
# create an instance of ForecastGet200ResponseCurrentWeatherUnits from a dict
forecast_get200_response_current_weather_units_from_dict = ForecastGet200ResponseCurrentWeatherUnits.from_dict(forecast_get200_response_current_weather_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


