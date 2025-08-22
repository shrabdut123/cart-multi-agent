# order_capture_client.CheckoutBillingContactsApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_contact**](CheckoutBillingContactsApi.md#create_billing_contact) | **POST** /{retailUnit}/checkouts/{checkoutId}/billing-contacts | Service for adding new billing contacts
[**get_billing_contacts**](CheckoutBillingContactsApi.md#get_billing_contacts) | **GET** /{retailUnit}/checkouts/{checkoutId}/billing-contacts | Service for getting a single billing contacts
[**update_billing_contact**](CheckoutBillingContactsApi.md#update_billing_contact) | **PUT** /{retailUnit}/checkouts/{checkoutId}/billing-contacts/{id} | Service for updating billing contacts


# **create_billing_contact**
> CreateResource create_billing_contact(checkout_id, retail_unit, billing_contact_request)

Service for adding new billing contacts

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.billing_contact_request import BillingContactRequest
from order_capture_client.models.create_resource import CreateResource
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
    api_instance = order_capture_client.CheckoutBillingContactsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    billing_contact_request = order_capture_client.BillingContactRequest() # BillingContactRequest | 

    try:
        # Service for adding new billing contacts
        api_response = api_instance.create_billing_contact(checkout_id, retail_unit, billing_contact_request)
        print("The response of CheckoutBillingContactsApi->create_billing_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutBillingContactsApi->create_billing_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **billing_contact_request** | [**BillingContactRequest**](BillingContactRequest.md)|  | 

### Return type

[**CreateResource**](CreateResource.md)

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

# **get_billing_contacts**
> BillingContact get_billing_contacts(checkout_id, retail_unit)

Service for getting a single billing contacts

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.billing_contact import BillingContact
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
    api_instance = order_capture_client.CheckoutBillingContactsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Service for getting a single billing contacts
        api_response = api_instance.get_billing_contacts(checkout_id, retail_unit)
        print("The response of CheckoutBillingContactsApi->get_billing_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutBillingContactsApi->get_billing_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**BillingContact**](BillingContact.md)

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

# **update_billing_contact**
> BillingContact update_billing_contact(checkout_id, id, retail_unit, billing_contact_request)

Service for updating billing contacts

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.billing_contact import BillingContact
from order_capture_client.models.billing_contact_request import BillingContactRequest
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
    api_instance = order_capture_client.CheckoutBillingContactsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    id = 'id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    billing_contact_request = order_capture_client.BillingContactRequest() # BillingContactRequest | 

    try:
        # Service for updating billing contacts
        api_response = api_instance.update_billing_contact(checkout_id, id, retail_unit, billing_contact_request)
        print("The response of CheckoutBillingContactsApi->update_billing_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutBillingContactsApi->update_billing_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **billing_contact_request** | [**BillingContactRequest**](BillingContactRequest.md)|  | 

### Return type

[**BillingContact**](BillingContact.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 204 - Updating Successfully |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

