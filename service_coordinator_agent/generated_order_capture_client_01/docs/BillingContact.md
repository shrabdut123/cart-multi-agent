# BillingContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**second_surname** | **str** |  | [optional] 
**phonetic_first_name** | **str** |  | [optional] 
**phonetic_last_name** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**county** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**land_line_number** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**fiscal_code** | **str** |  | [optional] 
**tax_code** | **str** |  | [optional] 
**tax_code_type** | **str** |  | [optional] 
**recipient_code_type** | **str** | supports only NONE,EMAIL,CODE,NO_INVOICE | [optional] 
**recipient_code** | **str** | depends on recipientCodeType, if it is email, then value expected is email | [optional] 
**country_of_origin** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**alternate_collector_first_name** | **str** |  | [optional] 
**alternate_collector_sur_name** | **str** |  | [optional] 
**same_as_shipping_contact** | **bool** |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 
**business_info** | [**BusinessInfo**](BusinessInfo.md) |  | [optional] 

## Example

```python
from order_capture_client.models.billing_contact import BillingContact

# TODO update the JSON string below
json = "{}"
# create an instance of BillingContact from a JSON string
billing_contact_instance = BillingContact.from_json(json)
# print the JSON string representation of the object
print(BillingContact.to_json())

# convert the object into a dict
billing_contact_dict = billing_contact_instance.to_dict()
# create an instance of BillingContact from a dict
billing_contact_from_dict = BillingContact.from_dict(billing_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


