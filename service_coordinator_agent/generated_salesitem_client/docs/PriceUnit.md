# PriceUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_unit_texts** | [**List[PriceUnitText]**](PriceUnitText.md) |  | [optional] 

## Example

```python
from salesitem_client.models.price_unit import PriceUnit

# TODO update the JSON string below
json = "{}"
# create an instance of PriceUnit from a JSON string
price_unit_instance = PriceUnit.from_json(json)
# print the JSON string representation of the object
print(PriceUnit.to_json())

# convert the object into a dict
price_unit_dict = price_unit_instance.to_dict()
# create an instance of PriceUnit from a dict
price_unit_from_dict = PriceUnit.from_dict(price_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


