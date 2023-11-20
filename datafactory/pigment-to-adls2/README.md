# Pigment to ADLS Gen2
An Azure Data Factory pipeline template which demonstrates an example of obtaining a CSV export from Pigment's export API and storing the result in an ADLS Gen2 folder.

## Getting Started
### Pipeline Import Method
Use this if you're just interested in the pipeline without the linked services.

1. Create your Data Factory in Azure
2. Navigate to the Studio for the above factory
3. Open the template gallery 
4. Download and import the `Pigment to ADLS.zip` file contained in this folder
5. Fill in the template details, then save
6. The template will be in the gallery, select it and complete the linked services for ADLS Gen2 and Pigment Export. If you're unsure what these should look like, use the examples in the `src/linkedService` folder.

### GitHub Method
Use this if you want the full sample with linked services, datasets, etc.
Fork or clone this repo to your own and use it as the GitHub configuration source for your Factory when creating it. The examples in this repo use dummy data and therefore will need updating with your own.


## Usage
There are parameters and linked services which need to be configured before first run:

### Pipeline Parameters
When imported, take note of the following Pipeline Parameters which need your input before running:
* `PigmentViewId` - The Pigment view ID you wish to export from. This is found in the URL when looking at the view in the UI.
* `SecretIdentifierURL` - The URL pointing towards the Pigment Export API Key entry in Azure Key Vault. This is obtained from the `secret identifier` field when viewing the secret's entry.
* `ADLSFileSystem` - The file system within ADLS to store the file to.
* `ADLSDirectory` - The directory within the file system to store the file to.


### Additional Services:
This sample requires the following to be set up on your side:
1. Azure Key Vault for secret storage.
2. ADLS Gen2 for CSV export storage. 

If you do not intend to use these services, you'll need to edit the factory to support your alternative.