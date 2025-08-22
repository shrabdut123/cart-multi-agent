# salesitem_client.SalesPriceApi

All URIs are relative to *https://api.salesitem.ingka.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_sales_prices**](SalesPriceApi.md#get_item_sales_prices) | **GET** /salesprices/{classUnitType}/{classUnitCode} | Get sales price information of the choosen sales item. Used to communicate sales price information in sales and customer communication scenarios.
[**get_item_sales_prices_by_items**](SalesPriceApi.md#get_item_sales_prices_by_items) | **GET** /salesprices/{classUnitType}/{classUnitCode}/items/{itemNumbers} | Get sales price information of the choosen sales item. Used to communicate sales price information in sales and customer communication scenarios.


# **get_item_sales_prices**
> SalesPriceResponse get_item_sales_prices(class_unit_type, class_unit_code, item_nos, language_code=language_code)

Get sales price information of the choosen sales item. Used to communicate sales price information in sales and customer communication scenarios.

Get the current sales items sales price information for the given item key(s) for a specific class unit (currently Business Unit with correct identifier).

### Example

* Api Key Authentication (clientIDHeader):

```python
import salesitem_client
from salesitem_client.models.sales_price_response import SalesPriceResponse
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
    api_instance = salesitem_client.SalesPriceApi(api_client)
    class_unit_type = 'class_unit_type_example' # str | `classUnitType` can be either Retail Unit/Market (`ru`) or Store (`sto`). `classUnitType` and `classUnitCode` gives a context of Class Unit when invoking one of the Selling Range APIs.  When a Retail Unit is requested, it must be combined with a valid `classUnitCode` of a Retail Unit. For example, `SE` for Sweden or `DE` for Germany.  When a Store is requested, it must be combined with a valid `classUnitCode` of a Store. For example, `445` for the Malmö store.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    class_unit_code = 'class_unit_code_example' # str | `classUnitCode` is the unique identifier of a Class Unit when combined with a `classUnitType`.  A valid `classUnitCode` always has a pattern like `^([A-Z]|[0-9]){2,5}$`. Note that the Selling Range APIs are case insensitive when it comes to the `classUnitCode` path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    item_nos = 'item_nos_example' # str | Item number is an unique identifier of an IKEA item/product in the Selling Range APIs. The Selling Range APIs only support the `ART`, `SGR` and `SPR` item types and there is no overlap between item numbers when considering those item types.  The Selling Range APIs support between 1 (single request) and 50 (batch request) item numbers per request. Considering that caching is hard for batch requests, it is recommended to do concurrent single requests instead of a batch request. 
    language_code = 'language_code_example' # str | Language code filter to be used in returned content. Returns all if not defined. (optional)

    try:
        # Get sales price information of the choosen sales item. Used to communicate sales price information in sales and customer communication scenarios.
        api_response = api_instance.get_item_sales_prices(class_unit_type, class_unit_code, item_nos, language_code=language_code)
        print("The response of SalesPriceApi->get_item_sales_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesPriceApi->get_item_sales_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_unit_type** | **str**| &#x60;classUnitType&#x60; can be either Retail Unit/Market (&#x60;ru&#x60;) or Store (&#x60;sto&#x60;). &#x60;classUnitType&#x60; and &#x60;classUnitCode&#x60; gives a context of Class Unit when invoking one of the Selling Range APIs.  When a Retail Unit is requested, it must be combined with a valid &#x60;classUnitCode&#x60; of a Retail Unit. For example, &#x60;SE&#x60; for Sweden or &#x60;DE&#x60; for Germany.  When a Store is requested, it must be combined with a valid &#x60;classUnitCode&#x60; of a Store. For example, &#x60;445&#x60; for the Malmö store.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **class_unit_code** | **str**| &#x60;classUnitCode&#x60; is the unique identifier of a Class Unit when combined with a &#x60;classUnitType&#x60;.  A valid &#x60;classUnitCode&#x60; always has a pattern like &#x60;^([A-Z]|[0-9]){2,5}$&#x60;. Note that the Selling Range APIs are case insensitive when it comes to the &#x60;classUnitCode&#x60; path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **item_nos** | **str**| Item number is an unique identifier of an IKEA item/product in the Selling Range APIs. The Selling Range APIs only support the &#x60;ART&#x60;, &#x60;SGR&#x60; and &#x60;SPR&#x60; item types and there is no overlap between item numbers when considering those item types.  The Selling Range APIs support between 1 (single request) and 50 (batch request) item numbers per request. Considering that caching is hard for batch requests, it is recommended to do concurrent single requests instead of a batch request.  | 
 **language_code** | **str**| Language code filter to be used in returned content. Returns all if not defined. | [optional] 

### Return type

[**SalesPriceResponse**](SalesPriceResponse.md)

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

# **get_item_sales_prices_by_items**
> SalesPriceResponse get_item_sales_prices_by_items(class_unit_type, class_unit_code, item_numbers, language_code=language_code)

Get sales price information of the choosen sales item. Used to communicate sales price information in sales and customer communication scenarios.

**DEPRECATED!** Please use [`this version`](#/Sales%20Price) without /items/ in path.

Get the current sales items sales price information for the given item key(s) for a specific class unit (currently Business Unit with correct
identifier).


### Example

* Api Key Authentication (clientIDHeader):

```python
import salesitem_client
from salesitem_client.models.sales_price_response import SalesPriceResponse
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
    api_instance = salesitem_client.SalesPriceApi(api_client)
    class_unit_type = 'class_unit_type_example' # str | `classUnitType` can be either Retail Unit/Market (`ru`) or Store (`sto`). `classUnitType` and `classUnitCode` gives a context of Class Unit when invoking one of the Selling Range APIs.  When a Retail Unit is requested, it must be combined with a valid `classUnitCode` of a Retail Unit. For example, `SE` for Sweden or `DE` for Germany.  When a Store is requested, it must be combined with a valid `classUnitCode` of a Store. For example, `445` for the Malmö store.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    class_unit_code = 'class_unit_code_example' # str | `classUnitCode` is the unique identifier of a Class Unit when combined with a `classUnitType`.  A valid `classUnitCode` always has a pattern like `^([A-Z]|[0-9]){2,5}$`. Note that the Selling Range APIs are case insensitive when it comes to the `classUnitCode` path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    item_numbers = 'item_numbers_example' # str | **DEPRECATED:** All APIs having `itemNumbers` as a path parameter are to be considered as deprecated. Please use an equvivalent API having the `itemNos` query parameter.  Item number is an unique identifier of an IKEA item/product in the Selling Range APIs. The Selling Range APIs only support the `ART`, `SGR` and `SPR` item types and there is no overlap between item numbers when considering those item types.  The Selling Range APIs support between 1 (single request) and 50 (batch request) item numbers per request. Considering that caching is hard for batch requests, it is recommended to do concurrent single requests instead of a batch request. 
    language_code = 'language_code_example' # str | Language code filter to be used in returned content. Returns all if not defined. (optional)

    try:
        # Get sales price information of the choosen sales item. Used to communicate sales price information in sales and customer communication scenarios.
        api_response = api_instance.get_item_sales_prices_by_items(class_unit_type, class_unit_code, item_numbers, language_code=language_code)
        print("The response of SalesPriceApi->get_item_sales_prices_by_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesPriceApi->get_item_sales_prices_by_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_unit_type** | **str**| &#x60;classUnitType&#x60; can be either Retail Unit/Market (&#x60;ru&#x60;) or Store (&#x60;sto&#x60;). &#x60;classUnitType&#x60; and &#x60;classUnitCode&#x60; gives a context of Class Unit when invoking one of the Selling Range APIs.  When a Retail Unit is requested, it must be combined with a valid &#x60;classUnitCode&#x60; of a Retail Unit. For example, &#x60;SE&#x60; for Sweden or &#x60;DE&#x60; for Germany.  When a Store is requested, it must be combined with a valid &#x60;classUnitCode&#x60; of a Store. For example, &#x60;445&#x60; for the Malmö store.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **class_unit_code** | **str**| &#x60;classUnitCode&#x60; is the unique identifier of a Class Unit when combined with a &#x60;classUnitType&#x60;.  A valid &#x60;classUnitCode&#x60; always has a pattern like &#x60;^([A-Z]|[0-9]){2,5}$&#x60;. Note that the Selling Range APIs are case insensitive when it comes to the &#x60;classUnitCode&#x60; path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **item_numbers** | **str**| **DEPRECATED:** All APIs having &#x60;itemNumbers&#x60; as a path parameter are to be considered as deprecated. Please use an equvivalent API having the &#x60;itemNos&#x60; query parameter.  Item number is an unique identifier of an IKEA item/product in the Selling Range APIs. The Selling Range APIs only support the &#x60;ART&#x60;, &#x60;SGR&#x60; and &#x60;SPR&#x60; item types and there is no overlap between item numbers when considering those item types.  The Selling Range APIs support between 1 (single request) and 50 (batch request) item numbers per request. Considering that caching is hard for batch requests, it is recommended to do concurrent single requests instead of a batch request.  | 
 **language_code** | **str**| Language code filter to be used in returned content. Returns all if not defined. | [optional] 

### Return type

[**SalesPriceResponse**](SalesPriceResponse.md)

### Authorization

[clientIDHeader](../README.md#clientIDHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ikea.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**207** | Partial Success - one or many of the item numbers are not found. Assuming correctly formed request URL (i.e. request is actually reaching API provider). More information in error payload. |  -  |
**400** | Bad Request. Typically if one of the input parameters is found incorrect. |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found - none of the item numbers are found. Assuming correctly formed request URL (i.e. request is actually reaching API provider). More information in error payload. |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

