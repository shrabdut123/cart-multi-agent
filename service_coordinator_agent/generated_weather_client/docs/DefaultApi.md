# weather_client.DefaultApi

All URIs are relative to *https://api.open-meteo.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_get**](DefaultApi.md#forecast_get) | **GET** /forecast | Get weather forecast


# **forecast_get**
> ForecastGet200Response forecast_get(latitude, longitude, current_weather=current_weather)

Get weather forecast

Retrieve current weather data for a given latitude and longitude.

### Example


```python
import weather_client
from weather_client.models.forecast_get200_response import ForecastGet200Response
from weather_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.open-meteo.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weather_client.Configuration(
    host = "https://api.open-meteo.com/v1"
)


# Enter a context with an instance of the API client
with weather_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weather_client.DefaultApi(api_client)
    latitude = 48.8566 # float | 
    longitude = 2.333 # float | 
    current_weather = true # bool |  (optional)

    try:
        # Get weather forecast
        api_response = api_instance.forecast_get(latitude, longitude, current_weather=current_weather)
        print("The response of DefaultApi->forecast_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->forecast_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **float**|  | 
 **longitude** | **float**|  | 
 **current_weather** | **bool**|  | [optional] 

### Return type

[**ForecastGet200Response**](ForecastGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful weather data response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

