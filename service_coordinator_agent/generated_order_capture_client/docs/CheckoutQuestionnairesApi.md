# order_capture_client.CheckoutQuestionnairesApi

All URIs are relative to *https://dev.oc.ingka.com/ordercaptureapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_questionnaires**](CheckoutQuestionnairesApi.md#get_questionnaires) | **GET** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/selected-delivery-and-services/questionnaires | Service for getting delivery &amp; service questionnaires
[**patch_questionnaire_answers**](CheckoutQuestionnairesApi.md#patch_questionnaire_answers) | **PATCH** /{retailUnit}/checkouts/{checkoutId}/service-area/{serviceAreaId}/selected-delivery-and-services/questionnaires | Service to save the answered delivery &amp; service questions


# **get_questionnaires**
> Questions get_questionnaires(retail_unit, checkout_id, service_area_id)

Service for getting delivery & service questionnaires

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.questions import Questions
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
    api_instance = order_capture_client.CheckoutQuestionnairesApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    service_area_id = 'service_area_id_example' # str | 

    try:
        # Service for getting delivery & service questionnaires
        api_response = api_instance.get_questionnaires(retail_unit, checkout_id, service_area_id)
        print("The response of CheckoutQuestionnairesApi->get_questionnaires:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutQuestionnairesApi->get_questionnaires: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 
 **service_area_id** | **str**|  | 

### Return type

[**Questions**](Questions.md)

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

# **patch_questionnaire_answers**
> QuestionsAndAnswers patch_questionnaire_answers(retail_unit, checkout_id, service_area_id)

Service to save the answered delivery & service questions

### Example

* Api Key Authentication (Client-Id):
* Bearer Authentication (BearerAuth):

```python
import order_capture_client
from order_capture_client.models.questions_and_answers import QuestionsAndAnswers
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
    api_instance = order_capture_client.CheckoutQuestionnairesApi(api_client)
    retail_unit = 'retail_unit_example' # str | 
    checkout_id = 'checkout_id_example' # str | 
    service_area_id = 'service_area_id_example' # str | 

    try:
        # Service to save the answered delivery & service questions
        api_response = api_instance.patch_questionnaire_answers(retail_unit, checkout_id, service_area_id)
        print("The response of CheckoutQuestionnairesApi->patch_questionnaire_answers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutQuestionnairesApi->patch_questionnaire_answers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retail_unit** | **str**|  | 
 **checkout_id** | **str**|  | 
 **service_area_id** | **str**|  | 

### Return type

[**QuestionsAndAnswers**](QuestionsAndAnswers.md)

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

