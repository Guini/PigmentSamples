# Pigment Upsert to Salesforce
An Azure Data Factory pipeline template which demonstrates an example of obtaining a CSV export from Pigment's export API and calling Salesforce to upsert the data to the opportunity object.

## Getting Started
### Pipeline Import Method
Use this if you're just interested in the pipeline without the linked services.

1. Create your Data Factory in Azure
2. Navigate to the Studio for the above factory
3. Open the template gallery 
4. Download and import the `Upsert From Pigment To Salesforce Opportunity.zip` file contained in this folder
5. Fill in the template details, then save
6. The template will be in the gallery, select it and complete the linked services for ADLS Gen2 and Pigment Export. If you're unsure what these should look like, use the examples in the `src/linkedService` folder.

### GitHub Method
Use this if you want the full sample with linked services, datasets, etc.
Fork or clone this repo to your own and use it as the GitHub configuration source for your Factory when creating it. The examples in this repo use dummy data and therefore will need updating with your own.


## Usage
There are parameters and linked services which need to be configured before first run, in addition you'll need to set up some linked services and ensure your Salesforce has an External ID field configured on your chosen object (in this example, the opportunity).

### Pipeline Parameters
When imported, take note of the following Pipeline Parameters which need your inpu before running:
* `PigmentViewId` - The Pigment view ID you wish to export from. This is found in the URL when looking at the view in the UI.
* `SecretIdentifierURL` - The URL pointing towards the Pigment Export API Key entry in Azure Key Vault. This is obtained from the `secret identifier` field when viewing the secret's entry.
* `SFDCUsername` - The email address of the Salesforce user the APIs will be run as. A service user is recommended.
* `SFDCExternalID` - The Salesforce API name of the field on the opportunity object which represents the External ID field. E.g. `External_ID__c`. This is not a standard field and needs to be created.


### Additional Services
This sample requires the following to be set up on your side:
1. Azure Key Vault for secret storage.
2. Salesforce with the opportunity object configured with the external ID field type.

If you do not intend to use these services, you'll need to edit the factory to support your alternative.

### Salesforce Setup
This sample uses the native Salesforce connector within Azure Data Factory. As it is using upsert, Salesforce requires the upserted object to have an External ID field in order to match and update records on. See the create an External ID field on the desired object article [here](https://help.salesforce.com/s/articleView?id=000383278&type=1) for information on how to create this field. It will need to be populated with the same value in both the view that's being exported in Pigment and in Salesforce.


If you do not intend to use upsert or the native connector provided by Azure, you will need to refer to the documentation for your chosen method and edit the sample accordingly.
