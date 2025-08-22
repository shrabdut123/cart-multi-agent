# order_capture_client.DeltaPriceControllerApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delta_prices_for_collect**](DeltaPriceControllerApi.md#get_delta_prices_for_collect) | **POST** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/delta-prices-collect | This API helps to calculate the delta prices of the PUP&#39;s under targetDelivery(targetDeliveryId would be sent in the request), based on the selected PUP&#39;s in previous deliveries
[**get_delta_prices_for_home_delivery**](DeltaPriceControllerApi.md#get_delta_prices_for_home_delivery) | **POST** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/delta-prices-hd | This API helps to calculate the delta prices of the Home delivery timeSlots under targetDelivery(targetDeliveryId would be sent in the request), based on the selected Home Delivery&#39;s in previous deliveries


# **get_delta_prices_for_collect**
> DeltaPriceResponseDto get_delta_prices_for_collect(retail_unit, service_area_id, checkout_id, selected_delivery_service_request)

This API helps to calculate the delta prices of the PUP's under targetDelivery(targetDeliveryId would be sent in the request), based on the selected PUP's in previous deliveries

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.delta_price_response_dto import DeltaPriceResponseDto
from order_capture_client.models.selected_delivery_service_request import SelectedDeliveryServiceRequest
from order_capture_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.oc.ingka.com/ordercaptureapi
# See configuration.py for a list of all supported configuration parameters.
configuration = order_capture_client.Configuration(
    host = "https://dev.oc.ingka.com/ordercaptureapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Client-Id
configuration.api_key['Client-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Client-Id'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = order_capture_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with order_capture_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_capture_client.DeltaPriceControllerApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    service_area_id = 'service_area_id_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    selected_delivery_service_request = order_capture_client.SelectedDeliveryServiceRequest() # SelectedDeliveryServiceRequest | 

    try:
        # This API helps to calculate the delta prices of the PUP's under targetDelivery(targetDeliveryId would be sent in the request), based on the selected PUP's in previous deliveries
        api_response = api_instance.get_delta_prices_for_collect(retail_unit, service_area_id, checkout_id, selected_delivery_service_request)
        print("The response of DeltaPriceControllerApi->get_delta_prices_for_collect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeltaPriceControllerApi->get_delta_prices_for_collect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **service_area_id** | **str**|  | 
 **checkout_id** | **str**|  | 
 **selected_delivery_service_request** | [**SelectedDeliveryServiceRequest**](SelectedDeliveryServiceRequest.md)|  | 

### Return type

[**DeltaPriceResponseDto**](DeltaPriceResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 - OK |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delta_prices_for_home_delivery**
> DeltaPriceTimeSlotResponseDto get_delta_prices_for_home_delivery(retail_unit, service_area_id, checkout_id, selected_delivery_service_request)

This API helps to calculate the delta prices of the Home delivery timeSlots under targetDelivery(targetDeliveryId would be sent in the request), based on the selected Home Delivery's in previous deliveries

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.delta_price_time_slot_response_dto import DeltaPriceTimeSlotResponseDto
from order_capture_client.models.selected_delivery_service_request import SelectedDeliveryServiceRequest
from order_capture_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.oc.ingka.com/ordercaptureapi
# See configuration.py for a list of all supported configuration parameters.
configuration = order_capture_client.Configuration(
    host = "https://dev.oc.ingka.com/ordercaptureapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Client-Id
configuration.api_key['Client-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Client-Id'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = order_capture_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with order_capture_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order_capture_client.DeltaPriceControllerApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    service_area_id = 'service_area_id_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    selected_delivery_service_request = order_capture_client.SelectedDeliveryServiceRequest() # SelectedDeliveryServiceRequest | 

    try:
        # This API helps to calculate the delta prices of the Home delivery timeSlots under targetDelivery(targetDeliveryId would be sent in the request), based on the selected Home Delivery's in previous deliveries
        api_response = api_instance.get_delta_prices_for_home_delivery(retail_unit, service_area_id, checkout_id, selected_delivery_service_request)
        print("The response of DeltaPriceControllerApi->get_delta_prices_for_home_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeltaPriceControllerApi->get_delta_prices_for_home_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **service_area_id** | **str**|  | 
 **checkout_id** | **str**|  | 
 **selected_delivery_service_request** | [**SelectedDeliveryServiceRequest**](SelectedDeliveryServiceRequest.md)|  | 

### Return type

[**DeltaPriceTimeSlotResponseDto**](DeltaPriceTimeSlotResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 - OK |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

