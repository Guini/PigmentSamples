# PigmentSamples
Unofficial samples using Pigment's API and third party serverless solutions.

See the readme within each directory for specific instructions for each sample.

# Pigment-to-S3 


An AWS Lambda example that exports one given block's data from Pigment into a specified S3 bucket. Uses AWS Secrets Manager for API key storage and Lambda enironment variables for some flexibility.

# Pigment-to-ADF

Two Azure Data Factory templates:
1. **pigment-to-adlsv2**: Exports from a view in Pigment and stores it within Azure Data Lake Storega Gen 2 (ADLSv2) in CSV format.
2. **pigment-to-sfdc**: Exports from a view in Pigment and `UPSERTS` the changes to Salesforce (SFDC). The example uses the Opportunity object, but it can be configured to use any object and can instead `INSERT` if preferred.


Both use Azure Key Vault for secrets storage (SFDC token, Pigment API Key), Azure IAM Service User for authorization to the other Azure services, Blob storage for the output and the default runtime configuration.
