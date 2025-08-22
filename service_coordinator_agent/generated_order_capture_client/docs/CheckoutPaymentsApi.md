# order_capture_client.CheckoutPaymentsApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_context**](CheckoutPaymentsApi.md#get_payment_context) | **GET** /{retailUnit}/checkouts/{checkoutId}/payment-context | Gets the payment context for the checkout
[**patch_express_pay_context_with_contact**](CheckoutPaymentsApi.md#patch_express_pay_context_with_contact) | **PATCH** /{retailUnit}/checkouts/{checkoutId}/express-payment-context/contact | Submits the full billing and shipping address to the express-payment-context, validates address information and initiates payment towards payment api.
[**patch_express_payment_context**](CheckoutPaymentsApi.md#patch_express_payment_context) | **PATCH** /{retailUnit}/checkouts/{checkoutId}/express-payment-context | Submits redacted address information from user payment account (i.e. Apple pay, Google pay or other wallet solutions) and validates against information previously submitted through the POST /deliveryAreas endpoint.
[**post_express_payment_context**](CheckoutPaymentsApi.md#post_express_payment_context) | **POST** /{retailUnit}/checkouts/{checkoutId}/express-payment-context | Creates express payment context for the checkout


# **get_payment_context**
> PaymentContext get_payment_context(retail_unit, checkout_id)

Gets the payment context for the checkout

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.payment_context import PaymentContext
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
    api_instance = order_capture_client.CheckoutPaymentsApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 

    try:
        # Gets the payment context for the checkout
        api_response = api_instance.get_payment_context(retail_unit, checkout_id)
        print("The response of CheckoutPaymentsApi->get_payment_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutPaymentsApi->get_payment_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 

### Return type

[**PaymentContext**](PaymentContext.md)

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

# **patch_express_pay_context_with_contact**
> ExpressPayContext patch_express_pay_context_with_contact(retail_unit, checkout_id, express_pay_context_request)

Submits the full billing and shipping address to the express-payment-context, validates address information and initiates payment towards payment api.

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.express_pay_context import ExpressPayContext
from order_capture_client.models.express_pay_context_request import ExpressPayContextRequest
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
    api_instance = order_capture_client.CheckoutPaymentsApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    express_pay_context_request = order_capture_client.ExpressPayContextRequest() # ExpressPayContextRequest | 

    try:
        # Submits the full billing and shipping address to the express-payment-context, validates address information and initiates payment towards payment api.
        api_response = api_instance.patch_express_pay_context_with_contact(retail_unit, checkout_id, express_pay_context_request)
        print("The response of CheckoutPaymentsApi->patch_express_pay_context_with_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutPaymentsApi->patch_express_pay_context_with_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 
 **express_pay_context_request** | [**ExpressPayContextRequest**](ExpressPayContextRequest.md)|  | 

### Return type

[**ExpressPayContext**](ExpressPayContext.md)

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

# **patch_express_payment_context**
> PaymentContext patch_express_payment_context(retail_unit, checkout_id, redacted_address_request)

Submits redacted address information from user payment account (i.e. Apple pay, Google pay or other wallet solutions) and validates against information previously submitted through the POST /deliveryAreas endpoint.

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.payment_context import PaymentContext
from order_capture_client.models.redacted_address_request import RedactedAddressRequest
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
    api_instance = order_capture_client.CheckoutPaymentsApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    redacted_address_request = order_capture_client.RedactedAddressRequest() # RedactedAddressRequest | 

    try:
        # Submits redacted address information from user payment account (i.e. Apple pay, Google pay or other wallet solutions) and validates against information previously submitted through the POST /deliveryAreas endpoint.
        api_response = api_instance.patch_express_payment_context(retail_unit, checkout_id, redacted_address_request)
        print("The response of CheckoutPaymentsApi->patch_express_payment_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutPaymentsApi->patch_express_payment_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 
 **redacted_address_request** | [**RedactedAddressRequest**](RedactedAddressRequest.md)|  | 

### Return type

[**PaymentContext**](PaymentContext.md)

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

# **post_express_payment_context**
> ExpressPayContext post_express_payment_context(retail_unit, checkout_id)

Creates express payment context for the checkout

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.express_pay_context import ExpressPayContext
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
    api_instance = order_capture_client.CheckoutPaymentsApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 

    try:
        # Creates express payment context for the checkout
        api_response = api_instance.post_express_payment_context(retail_unit, checkout_id)
        print("The response of CheckoutPaymentsApi->post_express_payment_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutPaymentsApi->post_express_payment_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 

### Return type

[**ExpressPayContext**](ExpressPayContext.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 - CREATED (note that redactedAddress, BillingContact and ShippingContact will be null at this stage). |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

