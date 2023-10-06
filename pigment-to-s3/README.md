# Pigment to S3 via AWS Lambda
_An unofficial sample using Pigment's API and AWS Lambda to Export CSV files to S3._

## Overview
Pigment does not natively offer connectors to export to external sources. This sample uses AWS Lambda to take a given Pigment block's metadata and pull a CSV copy to a specified S3 bucket.
This can be useful if a downstream warehouse/data lake offers S3 loads (e.g. Snowflake)

## Other Services Uused
1. AWS Secrets Manager for Pigment API Key storage
1. Lambda Environment Variables for some flexibility
1. _[Not used but recommended]_ AWS Cloud Watch for timer trigger
1. AWS IAM Manager to ensure Lambda can read/writw to the services here

## Usage
1. Create an Export API Key in Pigment, see their documentation [here](https://community.gopigment.com/security-permissions-82/manage-api-keys-226) on how to do this.
1. Create a new AWS Secrets Manager entry and add your Pigment Export Key in there.
1. Create a new AWS Lambda project, add the following as environment variables:
    - `APP_ID` = Your Pigment App Id
    - `AWS_SECRET_NAME` = The secret name that corresponds to the Export API Key in AWS Secrets Manager (e.g. PigmentExportKey)
    - `AWS_SECRET_REGION` = The region your AWS Secrets Manager entry resides in (e.g. us-east-1)
    - `S3_BUCKET_NAME` = The name of your S3 bucket that will hold the files
    - `SECRET_KEY` = The secret key corresponding to your Pigment Export API Key entry in AWS Secrets Manager
    - `VIEW_ID` = View Id of the block you want to export from Pigment (e.g. `685f2c0a-be27-4edd-ac58-54eade3336de`)
1. Configure AWS IAM manager so your Lambda project's IAM user can read/write to S3 and read from Secrets Manager. You can use either a role or a policy depending on your orgnisation's security/access management policy.
1. Add the python code, deploy & test. If successful, you'll find a folder in your S3 bucket corresponding to the ISO 8601 date/time when the test was run. Inside will be your CSV.

## Notes
* If you want to pull multiple files, you can either duplicate the project or amend the code.
* Use of AWS Secrets Manager is optional but recommended for SDLC best practice.
* Timer triggers are limited in Lambda without use of AWS Cloud Watch. See their documentation for how to run this using Cloud Watch. Ensure you add CloudWatch to the IAM policy/role as necessary.

# Feedback/Issues
Feedback is welcome! Please submit any feedback or issues via the Issues tab in Github. A