# PigmentSamples
Unofficial samples using Pigment's API and third party serverless solutions.

**See the README within each directory for specific getting started instructions for each sample.**

# 🪣 Pigment to S3 


An AWS Lambda example that exports one given block's data from Pigment into a specified S3 bucket. Uses AWS Secrets Manager for API key storage and Lambda enironment variables for some flexibility.

# 🏭 Azure Data Factory

Two Azure Data Factory templates. Both use Azure Key Vault for secrets storage (SFDC token, Pigment API Key), Azure IAM Service User for authorization to the other Azure services, Blob storage for the output and the default runtime configuration.

## **pigment-to-adlsv2**

Exports from a view in Pigment and stores it within Azure Data Lake Storega Gen 2 (ADLSv2) in CSV format.


## **pigment-to-sfdc**: 

Exports from a view in Pigment and `UPSERTS` the changes to Salesforce (SFDC).

# 📣 Feedback & Contribution
Please use GitHub Issues for feedback, bugs, enhancements, or any other non-code contributions.

I highly encourage checking out the code examples and tinkering. I am open to merging new features, enhancements and fixes, as well as good insights on the topics demonstrated in these examples.