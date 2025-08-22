# order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_selected_delivery_and_service**](CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi.md#delete_selected_delivery_and_service) | **DELETE** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/selected-delivery-and-services | Service to remove the choices the consumer saved earlier
[**get_collect_delivery_services**](CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi.md#get_collect_delivery_services) | **GET** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/collect-delivery-services | Service for Customer to get all available Collect Delivery Services
[**get_delivery_time_windows**](CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi.md#get_delivery_time_windows) | **GET** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/delivery-services/{type}/{selectedDeliveryServiceId}/delivery-time-windows | Service for Customer to select choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.
[**get_home_delivery_services**](CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi.md#get_home_delivery_services) | **GET** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/home-delivery-services | Service for Customer to get all available Home Delivery Services
[**get_saved_selected_deliver_and_service**](CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi.md#get_saved_selected_deliver_and_service) | **GET** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/selected-delivery-and-services | Service for Customer to change choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.
[**get_service_time_windows**](CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi.md#get_service_time_windows) | **GET** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/delivery-services/{type}/{selectedDeliveryServiceId}/service-time-windows | Service for Customer to get the calendar time windows for a selected delivery service
[**save_selected_delivery_and_service**](CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi.md#save_selected_delivery_and_service) | **POST** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/selected-delivery-and-services | Service for Customer to select choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.


# **delete_selected_delivery_and_service**
> CheckoutDto delete_selected_delivery_and_service(retail_unit, service_area_id, checkout_id)

Service to remove the choices the consumer saved earlier

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.checkout_dto import CheckoutDto
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
    api_instance = order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    service_area_id = 'service_area_id_example' # str | 
    checkout_id = 'checkout_id_example' # str | 

    try:
        # Service to remove the choices the consumer saved earlier
        api_response = api_instance.delete_selected_delivery_and_service(retail_unit, service_area_id, checkout_id)
        print("The response of CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->delete_selected_delivery_and_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->delete_selected_delivery_and_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **service_area_id** | **str**|  | 
 **checkout_id** | **str**|  | 

### Return type

[**CheckoutDto**](CheckoutDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_collect_delivery_services**
> DSResponseDto get_collect_delivery_services(service_area_id, checkout_id, retail_unit)

Service for Customer to get all available Collect Delivery Services

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.ds_response_dto import DSResponseDto
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
    api_instance = order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(api_client)
    service_area_id = 'service_area_id_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Service for Customer to get all available Collect Delivery Services
        api_response = api_instance.get_collect_delivery_services(service_area_id, checkout_id, retail_unit)
        print("The response of CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_collect_delivery_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_collect_delivery_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_area_id** | **str**|  | 
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**DSResponseDto**](DSResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_delivery_time_windows**
> TWResponseDto get_delivery_time_windows(type, selected_delivery_service_id, selected_pick_up_point_ids, retail_unit, checkout_id, service_area_id)

Service for Customer to select choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.tw_response_dto import TWResponseDto
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
    api_instance = order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(api_client)
    type = 'type_example' # str | It refers to super type i.e. HOME_DELIVERY or COLLECT
    selected_delivery_service_id = 'selected_delivery_service_id_example' # str | The selected delivery service id for which the delivery time windows should be calculated
    selected_pick_up_point_ids = 'selected_pick_up_point_ids_example' # str | It is mandatory if it is COLLECT. It allows comma separated selected OC PUP ID per delivery. 2 PUP ID from same delivery should not be passed
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    service_area_id = 'service_area_id_example' # str | 

    try:
        # Service for Customer to select choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.
        api_response = api_instance.get_delivery_time_windows(type, selected_delivery_service_id, selected_pick_up_point_ids, retail_unit, checkout_id, service_area_id)
        print("The response of CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_delivery_time_windows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_delivery_time_windows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| It refers to super type i.e. HOME_DELIVERY or COLLECT | 
 **selected_delivery_service_id** | **str**| The selected delivery service id for which the delivery time windows should be calculated | 
 **selected_pick_up_point_ids** | **str**| It is mandatory if it is COLLECT. It allows comma separated selected OC PUP ID per delivery. 2 PUP ID from same delivery should not be passed | 
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 
 **service_area_id** | **str**|  | 

### Return type

[**TWResponseDto**](TWResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_home_delivery_services**
> DSResponseDto get_home_delivery_services(service_area_id, checkout_id, retail_unit)

Service for Customer to get all available Home Delivery Services

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.ds_response_dto import DSResponseDto
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
    api_instance = order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(api_client)
    service_area_id = 'service_area_id_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Service for Customer to get all available Home Delivery Services
        api_response = api_instance.get_home_delivery_services(service_area_id, checkout_id, retail_unit)
        print("The response of CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_home_delivery_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_home_delivery_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_area_id** | **str**|  | 
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**DSResponseDto**](DSResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_saved_selected_deliver_and_service**
> CreateUpdateDSResponseDto get_saved_selected_deliver_and_service(retail_unit, service_area_id, checkout_id)

Service for Customer to change choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.create_update_ds_response_dto import CreateUpdateDSResponseDto
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
    api_instance = order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    service_area_id = 'service_area_id_example' # str | 
    checkout_id = 'checkout_id_example' # str | 

    try:
        # Service for Customer to change choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.
        api_response = api_instance.get_saved_selected_deliver_and_service(retail_unit, service_area_id, checkout_id)
        print("The response of CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_saved_selected_deliver_and_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_saved_selected_deliver_and_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **service_area_id** | **str**|  | 
 **checkout_id** | **str**|  | 

### Return type

[**CreateUpdateDSResponseDto**](CreateUpdateDSResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_service_time_windows**
> STWResponseDto get_service_time_windows(type, selected_delivery_service_id, selected_delivery_time_window_ids, selected_pick_up_point_ids, retail_unit, checkout_id, service_area_id)

Service for Customer to get the calendar time windows for a selected delivery service

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.stw_response_dto import STWResponseDto
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
    api_instance = order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(api_client)
    type = 'type_example' # str | It refers to super type i.e. HOME_DELIVERY or COLLECT
    selected_delivery_service_id = 'selected_delivery_service_id_example' # str | The selected delivery service id for which the delivery time windows should be calculated
    selected_delivery_time_window_ids = ['selected_delivery_time_window_ids_example'] # List[str] | The selected delivery time window id of each delivery. It allows comma separated selected time window ID per delivery. 2 time window ID from same delivery should not be passed
    selected_pick_up_point_ids = 'selected_pick_up_point_ids_example' # str | It is mandatory if it is COLLECT. It allows comma separated selected OC PUP ID per delivery. 2 PUP ID from same delivery should not be passed
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    service_area_id = 'service_area_id_example' # str | 

    try:
        # Service for Customer to get the calendar time windows for a selected delivery service
        api_response = api_instance.get_service_time_windows(type, selected_delivery_service_id, selected_delivery_time_window_ids, selected_pick_up_point_ids, retail_unit, checkout_id, service_area_id)
        print("The response of CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_service_time_windows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->get_service_time_windows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| It refers to super type i.e. HOME_DELIVERY or COLLECT | 
 **selected_delivery_service_id** | **str**| The selected delivery service id for which the delivery time windows should be calculated | 
 **selected_delivery_time_window_ids** | [**List[str]**](str.md)| The selected delivery time window id of each delivery. It allows comma separated selected time window ID per delivery. 2 time window ID from same delivery should not be passed | 
 **selected_pick_up_point_ids** | **str**| It is mandatory if it is COLLECT. It allows comma separated selected OC PUP ID per delivery. 2 PUP ID from same delivery should not be passed | 
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 
 **service_area_id** | **str**|  | 

### Return type

[**STWResponseDto**](STWResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **save_selected_delivery_and_service**
> SaveSelectedDeliveryAndService200Response save_selected_delivery_and_service(retail_unit, service_area_id, checkout_id, selected_delivery_and_service_request_dto, version=version)

Service for Customer to select choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.save_selected_delivery_and_service200_response import SaveSelectedDeliveryAndService200Response
from order_capture_client.models.selected_delivery_and_service_request_dto import SelectedDeliveryAndServiceRequestDto
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
    api_instance = order_capture_client.CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    service_area_id = 'service_area_id_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    selected_delivery_and_service_request_dto = order_capture_client.SelectedDeliveryAndServiceRequestDto() # SelectedDeliveryAndServiceRequestDto | 
    version = 'v1' # str |  (optional) (default to 'v1')

    try:
        # Service for Customer to select choice of the delivery service and its time windows and also time windows for a selected service such as assembly, installation etc.
        api_response = api_instance.save_selected_delivery_and_service(retail_unit, service_area_id, checkout_id, selected_delivery_and_service_request_dto, version=version)
        print("The response of CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->save_selected_delivery_and_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutDeliverServicesDeliveryTimeWindowsServiceTimeWindowsApi->save_selected_delivery_and_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **service_area_id** | **str**|  | 
 **checkout_id** | **str**|  | 
 **selected_delivery_and_service_request_dto** | [**SelectedDeliveryAndServiceRequestDto**](SelectedDeliveryAndServiceRequestDto.md)|  | 
 **version** | **str**|  | [optional] [default to &#39;v1&#39;]

### Return type

[**SaveSelectedDeliveryAndService200Response**](SaveSelectedDeliveryAndService200Response.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 - OK |  * version - Pass the value as &#39;v2&#39; to get the CheckoutDto.class as response <br>  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

