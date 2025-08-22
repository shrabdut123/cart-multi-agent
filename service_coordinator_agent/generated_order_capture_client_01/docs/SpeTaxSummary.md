# SpeTaxSummary

It represents the tax summary list. This can be null under item lines. It is relevant to consume this property only under the price type ORDER_TOTAL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_type** | **str** |  | [optional] 
**total_tax_amount** | **float** |  | [optional] 
**tax_percent** | **float** |  | [optional] 

## Example

```python
from order_capture_client.models.spe_tax_summary import SpeTaxSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SpeTaxSummary from a JSON string
spe_tax_summary_instance = SpeTaxSummary.from_json(json)
# print the JSON string representation of the object
print(SpeTaxSummary.to_json())

# convert the object into a dict
spe_tax_summary_dict = spe_tax_summary_instance.to_dict()
# create an instance of SpeTaxSummary from a dict
spe_tax_summary_from_dict = SpeTaxSummary.from_dict(spe_tax_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


