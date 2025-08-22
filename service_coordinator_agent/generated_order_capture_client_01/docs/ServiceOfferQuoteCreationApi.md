# order_capture_client.ServiceOfferQuoteCreationApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_so_platform_quote**](ServiceOfferQuoteCreationApi.md#get_so_platform_quote) | **GET** /{retailUnit}/checkouts/{checkoutId}/so-platform-quote | This API shall be used to fetch the job url with additional service information. This API shall be operated in async or forceCreate with an optional query parameter. While in async mode(default), it returns a different possible status and based on that the result would be available


# **get_so_platform_quote**
> SOPlatformCreateResponseDto get_so_platform_quote(force_create, checkout_id, retail_unit)

This API shall be used to fetch the job url with additional service information. This API shall be operated in async or forceCreate with an optional query parameter. While in async mode(default), it returns a different possible status and based on that the result would be available

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.so_platform_create_response_dto import SOPlatformCreateResponseDto
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
    api_instance = order_capture_client.ServiceOfferQuoteCreationApi(api_client)
    force_create = True # bool | This is used to synchronously fetch the data. It is recommended to use forceCreate=true only when the API returns TIMED_OUT in default async mode
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # This API shall be used to fetch the job url with additional service information. This API shall be operated in async or forceCreate with an optional query parameter. While in async mode(default), it returns a different possible status and based on that the result would be available
        api_response = api_instance.get_so_platform_quote(force_create, checkout_id, retail_unit)
        print("The response of ServiceOfferQuoteCreationApi->get_so_platform_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceOfferQuoteCreationApi->get_so_platform_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_create** | **bool**| This is used to synchronously fetch the data. It is recommended to use forceCreate&#x3D;true only when the API returns TIMED_OUT in default async mode | 
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**SOPlatformCreateResponseDto**](SOPlatformCreateResponseDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | A 400 response is returned when this call is made when the checkout is in a wrong state. For example, if it is invoked immediately after checkout creation, it returns HTTP 400 |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

