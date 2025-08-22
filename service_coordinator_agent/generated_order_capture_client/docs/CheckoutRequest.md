# CheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shopping_type** | **str** | Determines the type of the checkout, whether it is created ONLINE or from STORE  | 
**channel** | **str** | Determines whether the checkout is initiated from MOBILE_APP or WEBAPP | 
**shopping_app_platform** | **str** | This is for order creation analytics. This will be sent to Selling             order creation. IKEAAPP_ should be aligned with channel i.e.             MOBILEAPP. If not passed, it defaults to WEB_BROWSER | [optional] 
**family_card_no** | **str** | An optional family card number, if any | [optional] 
**apply_employee_discount** | **bool** | In case the user is a co-worker, and wants to apply the 15% discount, applyEmployeeDiscount has to be true | [optional] 
**profile_type** | **str** | Determines the type of user, REGULAR or BUSINESS | [optional] 
**delivery_area** | [**DeliveryAreaRequest**](DeliveryAreaRequest.md) |  | [optional] 
**service_area** | [**ServiceAreaRequest**](ServiceAreaRequest.md) |  | [optional] 
**cart_check_sum** | **str** | CheckSum to be used for debugging to Ensure the Checkout matches the CART snapshot | [optional] 
**language_code** | **str** | The language code used within the checkout initiation | 
**consumer_info** | [**ConsumerInfo**](ConsumerInfo.md) |  | [optional] 
**items** | [**List[ItemRequest]**](ItemRequest.md) | List of items added to the cart and ready for checkout, Each item line should be unique and must not repeat. If there are 2             lines with same article number, it should be sent as one line with             sum of both quantity lines. The availability of the article line             must be verified before passing in | 
**service_items** | [**List[ServiceItemRequest]**](ServiceItemRequest.md) | List of selling services associated with the order, mandatory if a cart having both goods items and             service items that needs to be captured | [optional] 
**removal_service_items** | [**List[RemovalServiceItemRequest]**](RemovalServiceItemRequest.md) | List of selling services associated with the order, mandatory if a cart having both goods items and             service items that needs to be captured | [optional] 
**coupon** | [**CouponRequest**](CouponRequest.md) |  | [optional] 
**preliminary_address_info** | [**PreliminaryAddressInfoRequest**](PreliminaryAddressInfoRequest.md) |  | [optional] 
**shipping_contacts** | [**List[ShippingContactRequest]**](ShippingContactRequest.md) | Shipping Address details. For providing address details in case of No Stock Store Orders checkouts. | [optional] 
**vpc_codes** | **List[str]** | This field is not mandatory. If provided, it will be validated against a regular expression. VPC codes are planner codes that are supported by DEXF APIs that helps in the enrichment of this code. Downstream systems uses the code to look up more details about the code.Order capture will not establish relation of vpc codes to a connected item. | [optional] 
**consents** | **List[str]** | This field is for the provided services consents. It is a list of strings, one or more of TIPPING_HAZARD, TASKRABBIT, NEED_HELP. This should show only for the markets that have the consents enabled. | [optional] 

## Example

```python
from order_capture_client.models.checkout_request import CheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutRequest from a JSON string
checkout_request_instance = CheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CheckoutRequest.to_json())

# convert the object into a dict
checkout_request_dict = checkout_request_instance.to_dict()
# create an instance of CheckoutRequest from a dict
checkout_request_from_dict = CheckoutRequest.from_dict(checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


