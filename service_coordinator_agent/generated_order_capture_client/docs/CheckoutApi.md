# order_capture_client.CheckoutApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout**](CheckoutApi.md#create_checkout) | **POST** /{retailUnit}/checkouts | It creates a checkout with the contextual information provided. It fetches the goods price and goods total from SPE. If service items are present, then it also calculates the provided service price using SPE API
[**create_existing_order_checkout**](CheckoutApi.md#create_existing_order_checkout) | **POST** /{retailUnit}/existing-order-checkouts | Responsible for creating checkouts with shoppingType&#x3D;NO_STOCK_STORE_ORDER, after the items are back in stock, the rest of orchestration continues as normal checkout. The payload should contain some more details other than the normal checkout e.g. orderNumber, shippingDetails...etc
[**get_checkout**](CheckoutApi.md#get_checkout) | **GET** /{retailUnit}/checkouts/{checkoutId} | Gets the checkout object
[**get_consumer_info**](CheckoutApi.md#get_consumer_info) | **GET** /{retailUnit}/checkouts/{checkoutId}/consumerinfo | This GET API responds back with the consumer info complex type with which the checkout was created. This object helps consumer to take consumer specific actions. This API  contains immutable information i.e. what ever was set during checkout creation cannot be changed. It is  protected with user token similar to other API&#39;s though it does not contain any sensitive information
[**get_i_gift_order**](CheckoutApi.md#get_i_gift_order) | **GET** /{retailUnit}/checkouts/{checkoutId}/igiftorder | Gets the IGIFT checkout OrderObject with masked personal information
[**get_order**](CheckoutApi.md#get_order) | **GET** /{retailUnit}/checkouts/{checkoutId}/order | Gets the checkout OrderObject
[**get_user_contacts**](CheckoutApi.md#get_user_contacts) | **GET** /{retailUnit}/checkouts/user | Gets the User object, The User contacts will be retrieved from the latest checkout, and the shippingContact will only be retrived if the ZipCode requested in the query param matches the latest(last saved) deliveryArea ZipCode.
[**patch_checkout**](CheckoutApi.md#patch_checkout) | **PATCH** /{retailUnit}/checkouts/{checkoutId} | This operation allows to PATCH few properties of checkout such as familyCardNumber, profileType, languageCode, items. Items patching is conditional and it allows only to reduce the quantity of an item. It does not permit to increase the quantity of an existing item. Moreover this operation must not be used for adding new items in to the checkout. An attempt to increase the quantity or adding a new item would result in an error. The purposeof the items patching is to address the partial stock scenarios where there is a need to reduce the quantity of an item and remove the item if it is unavailable. Please note that if there are connected services, that would be adjusted or removed implicit. PATCH operation results in price changes. PATCHING of items would invalidates the delivery calculations that are calculated already and this applies to the payment contexts too. Consumers must read the state from the PATCH response or perform a GET order operation to update the local state
[**update_user**](CheckoutApi.md#update_user) | **PUT** /{retailUnit}/checkouts/{checkoutId}/user | Service for update user


# **create_checkout**
> CreateResource create_checkout(retail_unit, checkout_request)

It creates a checkout with the contextual information provided. It fetches the goods price and goods total from SPE. If service items are present, then it also calculates the provided service price using SPE API

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.checkout_request import CheckoutRequest
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
    api_instance = order_capture_client.CheckoutApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_request = order_capture_client.CheckoutRequest() # CheckoutRequest | 

    try:
        # It creates a checkout with the contextual information provided. It fetches the goods price and goods total from SPE. If service items are present, then it also calculates the provided service price using SPE API
        api_response = api_instance.create_checkout(retail_unit, checkout_request)
        print("The response of CheckoutApi->create_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->create_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_request** | [**CheckoutRequest**](CheckoutRequest.md)|  | 

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

# **create_existing_order_checkout**
> CreateResource create_existing_order_checkout(retail_unit, existing_order_checkout_request)

Responsible for creating checkouts with shoppingType=NO_STOCK_STORE_ORDER, after the items are back in stock, the rest of orchestration continues as normal checkout. The payload should contain some more details other than the normal checkout e.g. orderNumber, shippingDetails...etc

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.create_resource import CreateResource
from order_capture_client.models.existing_order_checkout_request import ExistingOrderCheckoutRequest
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
    api_instance = order_capture_client.CheckoutApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    existing_order_checkout_request = order_capture_client.ExistingOrderCheckoutRequest() # ExistingOrderCheckoutRequest | 

    try:
        # Responsible for creating checkouts with shoppingType=NO_STOCK_STORE_ORDER, after the items are back in stock, the rest of orchestration continues as normal checkout. The payload should contain some more details other than the normal checkout e.g. orderNumber, shippingDetails...etc
        api_response = api_instance.create_existing_order_checkout(retail_unit, existing_order_checkout_request)
        print("The response of CheckoutApi->create_existing_order_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->create_existing_order_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **existing_order_checkout_request** | [**ExistingOrderCheckoutRequest**](ExistingOrderCheckoutRequest.md)|  | 

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

# **get_checkout**
> CheckoutDto get_checkout(checkout_id, retail_unit, checkout)

Gets the checkout object

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.checkout import Checkout
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
    api_instance = order_capture_client.CheckoutApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    checkout = order_capture_client.Checkout() # Checkout | 

    try:
        # Gets the checkout object
        api_response = api_instance.get_checkout(checkout_id, retail_unit, checkout)
        print("The response of CheckoutApi->get_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->get_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **checkout** | [**Checkout**](.md)|  | 

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
**200** | 200 OK - Checkout Response with CheckoutID in the responsebody |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer_info**
> ConsumerContextInfoDto get_consumer_info(checkout_id, retail_unit)

This GET API responds back with the consumer info complex type with which the checkout was created. This object helps consumer to take consumer specific actions. This API  contains immutable information i.e. what ever was set during checkout creation cannot be changed. It is  protected with user token similar to other API's though it does not contain any sensitive information

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.consumer_context_info_dto import ConsumerContextInfoDto
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
    api_instance = order_capture_client.CheckoutApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # This GET API responds back with the consumer info complex type with which the checkout was created. This object helps consumer to take consumer specific actions. This API  contains immutable information i.e. what ever was set during checkout creation cannot be changed. It is  protected with user token similar to other API's though it does not contain any sensitive information
        api_response = api_instance.get_consumer_info(checkout_id, retail_unit)
        print("The response of CheckoutApi->get_consumer_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->get_consumer_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

### Return type

[**ConsumerContextInfoDto**](ConsumerContextInfoDto.md)

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
**401** | 401 Unauthorized |  -  |
**404** | 404 Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_i_gift_order**
> CheckoutDto get_i_gift_order(checkout_id, retail_unit)

Gets the IGIFT checkout OrderObject with masked personal information

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
    api_instance = order_capture_client.CheckoutApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Gets the IGIFT checkout OrderObject with masked personal information
        api_response = api_instance.get_i_gift_order(checkout_id, retail_unit)
        print("The response of CheckoutApi->get_i_gift_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->get_i_gift_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

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

# **get_order**
> CheckoutDto get_order(checkout_id, retail_unit)

Gets the checkout OrderObject

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
    api_instance = order_capture_client.CheckoutApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 

    try:
        # Gets the checkout OrderObject
        api_response = api_instance.get_order(checkout_id, retail_unit)
        print("The response of CheckoutApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 

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

# **get_user_contacts**
> User get_user_contacts(retail_unit, zipcode=zipcode)

Gets the User object, The User contacts will be retrieved from the latest checkout, and the shippingContact will only be retrived if the ZipCode requested in the query param matches the latest(last saved) deliveryArea ZipCode.

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.user import User
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
    api_instance = order_capture_client.CheckoutApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    zipcode = 'zipcode_example' # str |  (optional)

    try:
        # Gets the User object, The User contacts will be retrieved from the latest checkout, and the shippingContact will only be retrived if the ZipCode requested in the query param matches the latest(last saved) deliveryArea ZipCode.
        api_response = api_instance.get_user_contacts(retail_unit, zipcode=zipcode)
        print("The response of CheckoutApi->get_user_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->get_user_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **zipcode** | **str**|  | [optional] 

### Return type

[**User**](User.md)

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
**410** | 410 Gone |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_checkout**
> CheckoutDto patch_checkout(checkout_id, retail_unit, checkout_patch_request)

This operation allows to PATCH few properties of checkout such as familyCardNumber, profileType, languageCode, items. Items patching is conditional and it allows only to reduce the quantity of an item. It does not permit to increase the quantity of an existing item. Moreover this operation must not be used for adding new items in to the checkout. An attempt to increase the quantity or adding a new item would result in an error. The purposeof the items patching is to address the partial stock scenarios where there is a need to reduce the quantity of an item and remove the item if it is unavailable. Please note that if there are connected services, that would be adjusted or removed implicit. PATCH operation results in price changes. PATCHING of items would invalidates the delivery calculations that are calculated already and this applies to the payment contexts too. Consumers must read the state from the PATCH response or perform a GET order operation to update the local state

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.checkout_dto import CheckoutDto
from order_capture_client.models.checkout_patch_request import CheckoutPatchRequest
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
    api_instance = order_capture_client.CheckoutApi(api_client)
    checkout_id = 'checkout_id_example' # str | 
    retail_unit = 'retail_unit_example' # str | 
    checkout_patch_request = order_capture_client.CheckoutPatchRequest() # CheckoutPatchRequest | 

    try:
        # This operation allows to PATCH few properties of checkout such as familyCardNumber, profileType, languageCode, items. Items patching is conditional and it allows only to reduce the quantity of an item. It does not permit to increase the quantity of an existing item. Moreover this operation must not be used for adding new items in to the checkout. An attempt to increase the quantity or adding a new item would result in an error. The purposeof the items patching is to address the partial stock scenarios where there is a need to reduce the quantity of an item and remove the item if it is unavailable. Please note that if there are connected services, that would be adjusted or removed implicit. PATCH operation results in price changes. PATCHING of items would invalidates the delivery calculations that are calculated already and this applies to the payment contexts too. Consumers must read the state from the PATCH response or perform a GET order operation to update the local state
        api_response = api_instance.patch_checkout(checkout_id, retail_unit, checkout_patch_request)
        print("The response of CheckoutApi->patch_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->patch_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**|  | 
 **retail_unit** | **str**|  | 
 **checkout_patch_request** | [**CheckoutPatchRequest**](CheckoutPatchRequest.md)|  | 

### Return type

[**CheckoutDto**](CheckoutDto.md)

### Authorization

[Client-Id](../README.md#Client-Id), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK - Checkout Response with CheckoutID in the responsebody |  -  |
**400** | Bad input parameter |  -  |
**404** | 404 Not Found |  -  |
**419** | Authentication timeout |  -  |
**422** | If all items are removed as a result of PATCH with items, then 422 is returned. This happens if the PATCH with items comes with a quantity 0 for all items |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> CheckoutDto update_user(retail_unit, checkout_id, update_user)

Service for update user

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.checkout_dto import CheckoutDto
from order_capture_client.models.update_user import UpdateUser
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
    api_instance = order_capture_client.CheckoutApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    update_user = order_capture_client.UpdateUser() # UpdateUser | 

    try:
        # Service for update user
        api_response = api_instance.update_user(retail_unit, checkout_id, update_user)
        print("The response of CheckoutApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 
 **update_user** | [**UpdateUser**](UpdateUser.md)|  | 

### Return type

[**CheckoutDto**](CheckoutDto.md)

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
**410** | 410 Gone |  -  |
**419** | Authentication timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

