# AvailabilityClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] 
**type** | **str** | NB! CASH_AND_CARRY and HOME_DELIVERY types have been decommissioned from the API response and moved to the CIA API.  | 
**value** | **bool** |  | 

## Example

```python
from salesitem_client.models.availability_classification import AvailabilityClassification

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityClassification from a JSON string
availability_classification_instance = AvailabilityClassification.from_json(json)
# print the JSON string representation of the object
print(AvailabilityClassification.to_json())

# convert the object into a dict
availability_classification_dict = availability_classification_instance.to_dict()
# create an instance of AvailabilityClassification from a dict
availability_classification_from_dict = AvailabilityClassification.from_dict(availability_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


