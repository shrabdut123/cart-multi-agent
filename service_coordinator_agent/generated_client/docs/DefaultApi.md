# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_service_prices**](DefaultApi.md#fetch_service_prices) | **POST** /graphql | GraphQL endpoint


# **fetch_service_prices**
> Dict[str, object] fetch_service_prices(fetch_service_prices_request)

GraphQL endpoint

### Example


```python
import openapi_client
from openapi_client.models.fetch_service_prices_request import FetchServicePricesRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    fetch_service_prices_request = openapi_client.FetchServicePricesRequest() # FetchServicePricesRequest | 

    try:
        # GraphQL endpoint
        api_response = api_instance.fetch_service_prices(fetch_service_prices_request)
        print("The response of DefaultApi->fetch_service_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->fetch_service_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_service_prices_request** | [**FetchServicePricesRequest**](FetchServicePricesRequest.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful GraphQL response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

