# order_capture_client.CheckoutServiceAreaApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_area**](CheckoutServiceAreaApi.md#create_service_area) | **POST** /{retailUnit}/checkouts/{checkoutId}/service-area | Create a service area where delivery and other services such as assembly is required
[**delete_service_area**](CheckoutServiceAreaApi.md#delete_service_area) | **DELETE** /{retailUnit}/checkouts/{checkoutId}/service-area | Deletes the created service area, and all the associated delivery services
[**get_service_area**](CheckoutServiceAreaApi.md#get_service_area) | **GET** /{retailUnit}/checkouts/{checkoutId}/service-area | Get the created service area


# **create_service_area**
> ServiceArea create_service_area(checkout_id, retail_unit, service_area_request)

Create a service area where delivery and other services such as assembly is required

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.service_area import ServiceArea
from order_capture_client.models.service_area_request import ServiceAreaRequest
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
    api_instance = order_capture_client.CheckoutServiceAreaApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    service_area_request = order_capture_client.ServiceAreaRequest() # ServiceAreaRequest | 

    try:
        # Create a service area where delivery and other services such as assembly is required
        api_response = api_instance.create_service_area(checkout_id, retail_unit, service_area_request)
        print("The response of CheckoutServiceAreaApi->create_service_area:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutServiceAreaApi->create_service_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **service_area_request** | [**ServiceAreaRequest**](ServiceAreaRequest.md)|  | 

### Return type

[**ServiceArea**](ServiceArea.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 - Created |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_area**
> delete_service_area(checkout_id, retail_unit, version=version)

Deletes the created service area, and all the associated delivery services

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
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
    api_instance = order_capture_client.CheckoutServiceAreaApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    version = 'v1' # str |  (optional) (default to 'v1')

    try:
        # Deletes the created service area, and all the associated delivery services
        api_instance.delete_service_area(checkout_id, retail_unit, version=version)
    except Exception as e:
        print("Exception when calling CheckoutServiceAreaApi->delete_service_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **version** | **str**|  | [optional] [default to &#39;v1&#39;]

### Return type

void (empty response body)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 - Updated Successfully |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_area**
> ServiceArea get_service_area(checkout_id, retail_unit)

Get the created service area

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.service_area import ServiceArea
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
    api_instance = order_capture_client.CheckoutServiceAreaApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Get the created service area
        api_response = api_instance.get_service_area(checkout_id, retail_unit)
        print("The response of CheckoutServiceAreaApi->get_service_area:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutServiceAreaApi->get_service_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**ServiceArea**](ServiceArea.md)

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

