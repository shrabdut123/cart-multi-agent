# CheckoutDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_id** | **str** |  | [optional] 
**shopping_type** | **str** |  | 
**user_id** | **str** |  | [optional] 
**user_type** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**shopping_app_platform** | **str** |  | [optional] 
**family_card_no** | **str** |  | [optional] 
**profile_type** | **str** |  | [optional] 
**service_area** | [**ServiceArea**](ServiceArea.md) |  | [optional] 
**apply_employee_discount** | **bool** |  | [optional] 
**employee_id** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**cart_check_sum** | **str** |  | [optional] 
**currency** | **str** | The currency | [optional] 
**retail_id** | **str** |  | [optional] 
**order_number** | **str** |  | [optional] 
**order_number_source** | **str** |  | [optional] 
**payment_context_id** | **str** |  | [optional] 
**deleted_payment_context_ids** | **List[str]** |  | [optional] 
**language_code** | **str** |  | [optional] 
**delivery_and_services** | [**DeliveryAndServiceEntity**](DeliveryAndServiceEntity.md) |  | [optional] 
**total_price** | [**Price**](Price.md) |  | [optional] 
**shipping_price** | [**Price**](Price.md) |  | [optional] 
**service_price** | [**Price**](Price.md) |  | [optional] 
**consumer_info** | [**ConsumerInfoDto**](ConsumerInfoDto.md) |  | [optional] 
**order_total** | [**Price**](Price.md) |  | [optional] 
**items** | [**List[ItemDto]**](ItemDto.md) |  | [optional] 
**service_items** | [**List[ServiceItem]**](ServiceItem.md) |  | [optional] 
**removal_service_items** | [**List[RemovalServiceItem]**](RemovalServiceItem.md) |  | [optional] 
**billing_contacts** | [**List[BillingContact]**](BillingContact.md) |  | [optional] 
**shipping_contacts** | [**List[ShippingContact]**](ShippingContact.md) |  | [optional] 
**payment** | [**Payment**](Payment.md) |  | [optional] 
**state** | **str** |  | [optional] 
**coupon** | [**Coupon**](Coupon.md) |  | [optional] 
**time_zone_id** | **str** |  | [optional] 
**selling_unit_type** | **str** |  | [optional] 
**selling_unit_code** | **str** |  | [optional] 
**coupon_info_list** | [**List[CouponInfo]**](CouponInfo.md) |  | [optional] 
**spe_coupons** | [**List[SpeCoupon]**](SpeCoupon.md) |  | [optional] 
**express_pay_context** | [**ExpressPayContext**](ExpressPayContext.md) |  | [optional] 
**service_offers** | [**List[ServiceOffer]**](ServiceOffer.md) |  | [optional] 
**ebv_order** | **bool** |  | [optional] 
**delivery_and_service_questionnaire_answers** | [**QuestionsAndAnswers**](QuestionsAndAnswers.md) |  | [optional] 
**use_sop_create_order** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 
**vpc_codes** | **List[str]** |  | [optional] 
**preliminary_address_info** | [**PreliminaryAddressInfo**](PreliminaryAddressInfo.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**checkout_expiry_metadata** | [**CheckoutExpiryMetadata**](CheckoutExpiryMetadata.md) |  | [optional] 
**consents** | **List[str]** |  | [optional] 
**validation_rules** | [**ValidationRules**](ValidationRules.md) |  | [optional] 

## Example

```python
from order_capture_client.models.checkout_dto import CheckoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutDto from a JSON string
checkout_dto_instance = CheckoutDto.from_json(json)
# print the JSON string representation of the object
print(CheckoutDto.to_json())

# convert the object into a dict
checkout_dto_dict = checkout_dto_instance.to_dict()
# create an instance of CheckoutDto from a dict
checkout_dto_from_dict = CheckoutDto.from_dict(checkout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


