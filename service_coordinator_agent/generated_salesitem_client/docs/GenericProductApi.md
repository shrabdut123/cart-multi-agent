# salesitem_client.GenericProductApi

All URIs are relative to *https://api.salesitem.ingka.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_generic_product_communication**](GenericProductApi.md#get_generic_product_communication) | **GET** /genericproducts/{classUnitType}/{classUnitCode} | Get Generic Product communication.


# **get_generic_product_communication**
> GenericProductResponse get_generic_product_communication(class_unit_type, class_unit_code, gpr_nos, language_code=language_code)

Get Generic Product communication.

Get generic product communication.

### Example

* Api Key Authentication (clientIDHeader):

```python
import salesitem_client
from salesitem_client.models.generic_product_response import GenericProductResponse
from salesitem_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.salesitem.ingka.com
# See configuration.py for a list of all supported configuration parameters.
configuration = salesitem_client.Configuration(
    host = "https://api.salesitem.ingka.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: clientIDHeader
configuration.api_key['clientIDHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['clientIDHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with salesitem_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = salesitem_client.GenericProductApi(api_client)
    class_unit_type = 'class_unit_type_example' # str | `classUnitType` can be either Retail Unit/Market (`ru`) or Store (`sto`). `classUnitType` and `classUnitCode` gives a context of Class Unit when invoking one of the Selling Range APIs.  When a Retail Unit is requested, it must be combined with a valid `classUnitCode` of a Retail Unit. For example, `SE` for Sweden or `DE` for Germany.  When a Store is requested, it must be combined with a valid `classUnitCode` of a Store. For example, `445` for the Malmö store.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    class_unit_code = 'class_unit_code_example' # str | `classUnitCode` is the unique identifier of a Class Unit when combined with a `classUnitType`.  A valid `classUnitCode` always has a pattern like `^([A-Z]|[0-9]){2,5}$`. Note that the Selling Range APIs are case insensitive when it comes to the `classUnitCode` path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    gpr_nos = 'gpr_nos_example' # str | One or many gpr numbers (maximum 50). If more than one - separated by commas
    language_code = 'language_code_example' # str | Language code filter to be used in returned content. Returns all if not defined. (optional)

    try:
        # Get Generic Product communication.
        api_response = api_instance.get_generic_product_communication(class_unit_type, class_unit_code, gpr_nos, language_code=language_code)
        print("The response of GenericProductApi->get_generic_product_communication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericProductApi->get_generic_product_communication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_unit_type** | **str**| &#x60;classUnitType&#x60; can be either Retail Unit/Market (&#x60;ru&#x60;) or Store (&#x60;sto&#x60;). &#x60;classUnitType&#x60; and &#x60;classUnitCode&#x60; gives a context of Class Unit when invoking one of the Selling Range APIs.  When a Retail Unit is requested, it must be combined with a valid &#x60;classUnitCode&#x60; of a Retail Unit. For example, &#x60;SE&#x60; for Sweden or &#x60;DE&#x60; for Germany.  When a Store is requested, it must be combined with a valid &#x60;classUnitCode&#x60; of a Store. For example, &#x60;445&#x60; for the Malmö store.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **class_unit_code** | **str**| &#x60;classUnitCode&#x60; is the unique identifier of a Class Unit when combined with a &#x60;classUnitType&#x60;.  A valid &#x60;classUnitCode&#x60; always has a pattern like &#x60;^([A-Z]|[0-9]){2,5}$&#x60;. Note that the Selling Range APIs are case insensitive when it comes to the &#x60;classUnitCode&#x60; path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **gpr_nos** | **str**| One or many gpr numbers (maximum 50). If more than one - separated by commas | 
 **language_code** | **str**| Language code filter to be used in returned content. Returns all if not defined. | [optional] 

### Return type

[**GenericProductResponse**](GenericProductResponse.md)

### Authorization

[clientIDHeader](../README.md#clientIDHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ikea.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request. Typically if one of the input parameters is found incorrect. |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

