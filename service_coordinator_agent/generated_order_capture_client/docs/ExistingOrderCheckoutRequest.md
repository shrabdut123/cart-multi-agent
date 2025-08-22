# ExistingOrderCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Determines whether the checkout is initiated from MOBILE_APP or WEBAPP | 
**shopping_app_platform** | **str** | This is for order creation analytics. This will be sent to Selling             order creation. IKEAAPP_ should be aligned with channel i.e.             MOBILEAPP. If not passed, it defaults to WEB_BROWSER | [optional] 
**family_card_no** | **str** | An optional family card number, if any | [optional] 
**profile_type** | **str** | Determines the type of user, REGULAR or BUSINESS | [optional] 
**language_code** | **str** | The language code used within the checkout initiation | 
**order_number** | **str** | Mandatory in case of No stock store orders, as this checkout should trigger an order modification. | 
**order_number_source** | **str** | Source of the orderNumber, varies per region. Mandatory in case of No stock store orders, as this checkout should trigger an order modification. | 
**items** | [**List[ItemRequest]**](ItemRequest.md) | List of items added to the cart and ready for checkout, Each item line should be unique and must not repeat. If there are 2             lines with same article number, it should be sent as one line with             sum of both quantity lines. The availability of the article line             must be verified before passing in | 
**coupon** | [**CouponRequest**](CouponRequest.md) |  | [optional] 
**shipping_contacts** | [**List[ShippingContact]**](ShippingContact.md) | Shipping Address details. For providing address details in case of No Stock Store Orders checkouts. | [optional] 
**billing_contacts** | [**List[BillingContact]**](BillingContact.md) | Billing Address details. For providing billing info in case of No Stock Store Orders checkouts. | [optional] 
**delivery_and_service_questionnaire_answers** | [**QuestionsAndAnswers**](QuestionsAndAnswers.md) |  | [optional] 
**version** | **str** | Order version in iSell, only used for modification scenarios | [optional] 
**consumer_info** | [**ConsumerInfo**](ConsumerInfo.md) |  | [optional] 
**bu_code** | **str** |  | [optional] 

## Example

```python
from order_capture_client.models.existing_order_checkout_request import ExistingOrderCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingOrderCheckoutRequest from a JSON string
existing_order_checkout_request_instance = ExistingOrderCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(ExistingOrderCheckoutRequest.to_json())

# convert the object into a dict
existing_order_checkout_request_dict = existing_order_checkout_request_instance.to_dict()
# create an instance of ExistingOrderCheckoutRequest from a dict
existing_order_checkout_request_from_dict = ExistingOrderCheckoutRequest.from_dict(existing_order_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


