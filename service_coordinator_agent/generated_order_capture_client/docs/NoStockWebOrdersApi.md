# order_capture_client.NoStockWebOrdersApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_no_stock_web_order**](NoStockWebOrdersApi.md#create_no_stock_web_order) | **GET** /{retailUnit}/checkouts/{checkoutId}/no-stock-order | Endpoint for publishing a message to oc-events topic to confirm completion of a no-stock/waiting list order


# **create_no_stock_web_order**
> create_no_stock_web_order(retail_unit, checkout_id)

Endpoint for publishing a message to oc-events topic to confirm completion of a no-stock/waiting list order

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
    api_instance = order_capture_client.NoStockWebOrdersApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 

    try:
        # Endpoint for publishing a message to oc-events topic to confirm completion of a no-stock/waiting list order
        api_instance.create_no_stock_web_order(retail_unit, checkout_id)
    except Exception as e:
        print("Exception when calling NoStockWebOrdersApi->create_no_stock_web_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 - OK |  -  |
**400** | Bad input parameter |  -  |
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

