# order_capture_client.CheckoutItemsApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item**](CheckoutItemsApi.md#get_item) | **GET** /{retailUnit}/checkouts/{checkoutId}/items/{itemId} | Service for viewing single item
[**get_items**](CheckoutItemsApi.md#get_items) | **GET** /{retailUnit}/checkouts/{checkoutId}/items | Service for viewing all items


# **get_item**
> ItemDto get_item(checkout_id, item_id, retail_unit)

Service for viewing single item

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.item_dto import ItemDto
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
    api_instance = order_capture_client.CheckoutItemsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    item_id = 'item_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Service for viewing single item
        api_response = api_instance.get_item(checkout_id, item_id, retail_unit)
        print("The response of CheckoutItemsApi->get_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutItemsApi->get_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **item_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**ItemDto**](ItemDto.md)

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

# **get_items**
> List[ItemDto] get_items(checkout_id, retail_unit)

Service for viewing all items

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.item_dto import ItemDto
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
    api_instance = order_capture_client.CheckoutItemsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Service for viewing all items
        api_response = api_instance.get_items(checkout_id, retail_unit)
        print("The response of CheckoutItemsApi->get_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutItemsApi->get_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**List[ItemDto]**](ItemDto.md)

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

