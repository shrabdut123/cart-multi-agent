# salesitem_client.AvailabilityClassificationApi

All URIs are relative to *https://api.salesitem.ingka.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_availability_classifications**](AvailabilityClassificationApi.md#get_item_availability_classifications) | **GET** /availabilityclassifications/{classUnitType}/{classUnitCode} | Get availability classification information (operational range) of the choosen class unit. Used to get a complete list of items based on at least one classification type. Please note that you have to specify either the &#x60;itemNos&#x60; query parameter or the &#x60;type&#x60; query parameter.


# **get_item_availability_classifications**
> AvailabilityClassificationResponse get_item_availability_classifications(class_unit_type, class_unit_code, channel=channel, type=type, item_nos=item_nos, value=value, item_type=item_type)

Get availability classification information (operational range) of the choosen class unit. Used to get a complete list of items based on at least one classification type. Please note that you have to specify either the `itemNos` query parameter or the `type` query parameter.

Get the current list of itemsAvailabilityClassifications

### Example

* Api Key Authentication (clientIDHeader):

```python
import salesitem_client
from salesitem_client.models.availability_classification_response import AvailabilityClassificationResponse
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
    api_instance = salesitem_client.AvailabilityClassificationApi(api_client)
    class_unit_type = 'class_unit_type_example' # str | `classUnitType` must be Retail Unit (`ru`). It is used together with `classUnitCode` to give context when invoking AvailabilityClassifications API.  Retail Unit must be combined with a valid `classUnitCode`. For example, `SE` for Sweden or `DE` for Germany.  A list of valid Retail Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    class_unit_code = 'class_unit_code_example' # str | `classUnitCode` is the unique identifier of a Class Unit when combined with a `classUnitType`.  A valid `classUnitCode` always has a pattern like `^([A-Z]|[0-9]){2,5}$`. Note that the Selling Range APIs are case insensitive when it comes to the `classUnitCode` path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network). 
    channel = 'channel_example' # str | Optional filter to find a rule for a specific channel. If not passed all channels are returned. ALL indicates channel independent. (optional)
    type = 'type_example' # str | Optional filter to find a specific classification type. If not passed all types are returned. CASH_AND_CARRY and HOME_DELIVERY types have been decommissioned from the API response and moved to the CIA API. (optional)
    item_nos = 'item_nos_example' # str | One or many item numbers (maximum 50). If more than one - separated by commas (optional)
    value = True # bool | Optional filter to find a specific classification value, true or false. If not passed all values are returned. (optional)
    item_type = 'item_type_example' # str | Optional filter to find a specific item type. If not passed all types are returned. (optional)

    try:
        # Get availability classification information (operational range) of the choosen class unit. Used to get a complete list of items based on at least one classification type. Please note that you have to specify either the `itemNos` query parameter or the `type` query parameter.
        api_response = api_instance.get_item_availability_classifications(class_unit_type, class_unit_code, channel=channel, type=type, item_nos=item_nos, value=value, item_type=item_type)
        print("The response of AvailabilityClassificationApi->get_item_availability_classifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityClassificationApi->get_item_availability_classifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_unit_type** | **str**| &#x60;classUnitType&#x60; must be Retail Unit (&#x60;ru&#x60;). It is used together with &#x60;classUnitCode&#x60; to give context when invoking AvailabilityClassifications API.  Retail Unit must be combined with a valid &#x60;classUnitCode&#x60;. For example, &#x60;SE&#x60; for Sweden or &#x60;DE&#x60; for Germany.  A list of valid Retail Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **class_unit_code** | **str**| &#x60;classUnitCode&#x60; is the unique identifier of a Class Unit when combined with a &#x60;classUnitType&#x60;.  A valid &#x60;classUnitCode&#x60; always has a pattern like &#x60;^([A-Z]|[0-9]){2,5}$&#x60;. Note that the Selling Range APIs are case insensitive when it comes to the &#x60;classUnitCode&#x60; path parameter and lower case is always internally converted to upper case.  A list of valid Class Units can be found [in CBD](https://iwww.cbdview.ikea.com/) (requires VPN or internal network).  | 
 **channel** | **str**| Optional filter to find a rule for a specific channel. If not passed all channels are returned. ALL indicates channel independent. | [optional] 
 **type** | **str**| Optional filter to find a specific classification type. If not passed all types are returned. CASH_AND_CARRY and HOME_DELIVERY types have been decommissioned from the API response and moved to the CIA API. | [optional] 
 **item_nos** | **str**| One or many item numbers (maximum 50). If more than one - separated by commas | [optional] 
 **value** | **bool**| Optional filter to find a specific classification value, true or false. If not passed all values are returned. | [optional] 
 **item_type** | **str**| Optional filter to find a specific item type. If not passed all types are returned. | [optional] 

### Return type

[**AvailabilityClassificationResponse**](AvailabilityClassificationResponse.md)

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

