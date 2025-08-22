# order_capture_client.CheckoutShippingContactsApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_contact**](CheckoutShippingContactsApi.md#create_shipping_contact) | **POST** /{retailUnit}/checkouts/{checkoutId}/shipping-contacts | Service for adding new shipping contacts
[**get_shipping_contacts**](CheckoutShippingContactsApi.md#get_shipping_contacts) | **GET** /{retailUnit}/checkouts/{checkoutId}/shipping-contacts | Shipping Address details. For providing address details in case of No Stock Store Orders checkouts.
[**update_shipping_contact**](CheckoutShippingContactsApi.md#update_shipping_contact) | **PUT** /{retailUnit}/checkouts/{checkoutId}/shipping-contacts/{id} | Service for updating shipping contact


# **create_shipping_contact**
> CreateResource create_shipping_contact(checkout_id, retail_unit, shipping_contact_request)

Service for adding new shipping contacts

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.create_resource import CreateResource
from order_capture_client.models.shipping_contact_request import ShippingContactRequest
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
    api_instance = order_capture_client.CheckoutShippingContactsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    shipping_contact_request = order_capture_client.ShippingContactRequest() # ShippingContactRequest | 

    try:
        # Service for adding new shipping contacts
        api_response = api_instance.create_shipping_contact(checkout_id, retail_unit, shipping_contact_request)
        print("The response of CheckoutShippingContactsApi->create_shipping_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutShippingContactsApi->create_shipping_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **shipping_contact_request** | [**ShippingContactRequest**](ShippingContactRequest.md)|  | 

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

# **get_shipping_contacts**
> CreateResource get_shipping_contacts(checkout_id, retail_unit, zipcode=zipcode)

Shipping Address details. For providing address details in case of No Stock Store Orders checkouts.

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
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
    api_instance = order_capture_client.CheckoutShippingContactsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    zipcode = 'zipcode_example' # str |  (optional)

    try:
        # Shipping Address details. For providing address details in case of No Stock Store Orders checkouts.
        api_response = api_instance.get_shipping_contacts(checkout_id, retail_unit, zipcode=zipcode)
        print("The response of CheckoutShippingContactsApi->get_shipping_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutShippingContactsApi->get_shipping_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **zipcode** | **str**|  | [optional] 

### Return type

[**CreateResource**](CreateResource.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 200 - OK |  -  |
**400** | Bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_contact**
> ShippingContact update_shipping_contact(checkout_id, id, retail_unit, shipping_contact_request)

Service for updating shipping contact

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.shipping_contact import ShippingContact
from order_capture_client.models.shipping_contact_request import ShippingContactRequest
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
    api_instance = order_capture_client.CheckoutShippingContactsApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    id = 'id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    shipping_contact_request = order_capture_client.ShippingContactRequest() # ShippingContactRequest | 

    try:
        # Service for updating shipping contact
        api_response = api_instance.update_shipping_contact(checkout_id, id, retail_unit, shipping_contact_request)
        print("The response of CheckoutShippingContactsApi->update_shipping_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutShippingContactsApi->update_shipping_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **shipping_contact_request** | [**ShippingContactRequest**](ShippingContactRequest.md)|  | 

### Return type

[**ShippingContact**](ShippingContact.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

