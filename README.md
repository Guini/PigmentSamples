# PigmentSamples
Unofficial samples using Pigment's API

See the readme within each directory for specific instructions for each sample.

# Pigment-to-S3 
[Link](https://github.com/Guini/PigmentSamples/tree/main/pigment-to-s3#readme)


An AWS Lambda example that exports one given block's data from Pigment into a specified S3 bucket. Uses AWS Secrets Manager for API key storage and Lambda enironment variables for some flexibility.

# Pigment-to-ADF
[Link](https://github.com/Guini/PigmentSamples/tree/main/pigment-to-adf)

An Azure Data Factory template demonstrating an export from a view in Pigment to Azure Data Lake Storega Gen 2 (ADLSv2). It uses Azure Key Vault for secrets storage, IAM for authorization to the other Azure services and Blob storage for the output.
