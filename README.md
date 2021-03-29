# related_parties_parsing_function

This project contains code for parsing and returning dates (years) from an Excel file within a sheet named 'YearRange'. 

## Environment Setup
Before running this project, create a `local.settings.json` file in the root directory. This file needs to have the following entries under the `values` section:

| Key | Value |
|-----|-------|
| AzureWebJobsStorage                 | The connection string to the storage account used by the Functions runtime.  To use the storage emulator, set the value to UseDevelopmentStorage=true |
| FUNCTIONS_WORKER_RUNTIME            | Set this value to `python` as this is a python Function App | 
| STORAGE_ACCOUNT_URL | Blob storage account URL for the storage account where Excel file has been uploaded |
| STORAGE_ACCOUNT_KEY | Blob storage account key for the storage account where Excel file has been uploaded |
| STORAGE_CONTAINER_NAME | Name of the storage container where Excel file has been uploaded |