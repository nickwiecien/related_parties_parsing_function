import logging
import pandas as pd
import json
import os
import tempfile
import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:

    
    #Parse body of request
    body = req.get_body()
    
    #Get 'name' attribute from json body
    #Note: name = container/filename
    blob_name = json.loads(body)['name']

    client = BlobServiceClient(os.environ.get('STORAGE_ACCOUNT_URL'), os.environ.get('STORAGE_ACCOUNT_KEY'))
    container_client = client.get_container_client(os.environ.get('STORAGE_CONTAINER_NAME'))
    blob_data = container_client.download_blob(blob_name)

    #Get temporary directory
    tempdir = tempfile.gettempdir()

    #Get uploaded file name
    filename = blob_name.split('/')[-1]

    #Write blob data to temporary file
    temp_path = os.path.join(tempdir, filename)
    with open(temp_path, 'wb') as file:
        file.write(blob_data.readall())

    #Read data from sheet named 'YearRange' in the uploaded excel file
    df = pd.read_excel(temp_path, sheet_name='YearRange')

    #Grab min_year and max_year from first row of data
    min_year = df.iloc[0]['min_year']
    max_year = df.iloc[0]['max_year']

    #Format JSON object to be returned with min/max years
    return_obj = {'min_year': int(min_year), 'max_year': int(max_year)}

    #Remove Excel file temporarily download to temp storage
    os.remove(temp_path)

    #Return result
    return func.HttpResponse(json.dumps(return_obj), status_code=200)
