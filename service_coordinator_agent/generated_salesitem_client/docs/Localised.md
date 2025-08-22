# Localised


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgement** | [**Acknowledgement**](Acknowledgement.md) |  | [optional] 
**assembly_effort** | [**List[AssemblyEffort]**](AssemblyEffort.md) |  | [optional] 
**attachments** | [**List[ItemAttachment]**](ItemAttachment.md) |  | [optional] 
**backoff_to_hero** | [**BackoffToHero**](BackoffToHero.md) |  | [optional] 
**benefit_summary** | **str** |  | [optional] 
**benefits** | **List[str]** |  | [optional] 
**care_instructions** | [**List[ItemCareInstruction]**](ItemCareInstruction.md) |  | [optional] 
**certification_media** | [**List[CertificationMedia]**](CertificationMedia.md) |  | [optional] 
**compliance** | [**List[Compliance]**](Compliance.md) |  | [optional] 
**compliance_information** | [**List[ComplianceInformation]**](ComplianceInformation.md) |  | [optional] 
**country_code** | **str** |  | [optional] 
**designers** | [**List[Designer]**](Designer.md) |  | [optional] 
**display_unit** | [**DisplayUnit**](DisplayUnit.md) |  | [optional] 
**environment_texts** | [**List[ItemEnvironmentText]**](ItemEnvironmentText.md) |  | [optional] 
**filter_information** | [**FilterInformation**](FilterInformation.md) |  | [optional] 
**full_length_texts** | [**FullLengthText**](FullLengthText.md) |  | [optional] 
**good_to_knows** | [**List[ItemGoodToKnow]**](ItemGoodToKnow.md) |  | [optional] 
**item_name_local** | **str** |  | [optional] 
**key_benefits** | [**List[ItemKeyBenefit]**](ItemKeyBenefit.md) |  | [optional] 
**language_code** | **str** |  | [optional] 
**long_benefits** | [**List[ItemBenefit]**](ItemBenefit.md) |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**materials** | [**List[ItemCustomerMaterial]**](ItemCustomerMaterial.md) |  | [optional] 
**measurements** | [**ItemMeasurements**](ItemMeasurements.md) |  | [optional] 
**media** | [**List[ItemMedia]**](ItemMedia.md) |  | [optional] 
**package_measurements** | [**List[ItemPackageMeasure]**](ItemPackageMeasure.md) |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_tags** | [**List[LocaleProductTag]**](LocaleProductTag.md) |  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 
**seo_slug** | **str** |  | [optional] 
**technical_compliance** | [**List[TechnicalCompliance]**](TechnicalCompliance.md) |  | [optional] 
**technical_information** | [**TechnicalInformation**](TechnicalInformation.md) |  | [optional] 
**valid_design** | [**ValidDesign**](ValidDesign.md) |  | [optional] 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**benefits_as_is** | **List[str]** |  | [optional] 
**benefit_summary_as_is** | **str** |  | [optional] 

## Example

```python
from salesitem_client.models.localised import Localised

# TODO update the JSON string below
json = "{}"
# create an instance of Localised from a JSON string
localised_instance = Localised.from_json(json)
# print the JSON string representation of the object
print(Localised.to_json())

# convert the object into a dict
localised_dict = localised_instance.to_dict()
# create an instance of Localised from a dict
localised_from_dict = Localised.from_dict(localised_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


