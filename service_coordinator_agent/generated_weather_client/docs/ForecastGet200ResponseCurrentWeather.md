# ForecastGet200ResponseCurrentWeather


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | [optional] 
**interval** | **int** |  | [optional] 
**temperature** | **float** |  | [optional] 
**windspeed** | **float** |  | [optional] 
**winddirection** | **int** |  | [optional] 
**is_day** | **int** |  | [optional] 
**weathercode** | **int** |  | [optional] 

## Example

```python
from weather_client.models.forecast_get200_response_current_weather import ForecastGet200ResponseCurrentWeather

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastGet200ResponseCurrentWeather from a JSON string
forecast_get200_response_current_weather_instance = ForecastGet200ResponseCurrentWeather.from_json(json)
# print the JSON string representation of the object
print(ForecastGet200ResponseCurrentWeather.to_json())

# convert the object into a dict
forecast_get200_response_current_weather_dict = forecast_get200_response_current_weather_instance.to_dict()
# create an instance of ForecastGet200ResponseCurrentWeather from a dict
forecast_get200_response_current_weather_from_dict = ForecastGet200ResponseCurrentWeather.from_dict(forecast_get200_response_current_weather_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


