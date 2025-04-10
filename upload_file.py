from dotenv import load_dotenv
import os

# Load from your custom env file
load_dotenv(".env")  # explicitly loading key.env

# Azure storage credentials
account_name = "saoneantra"
account_key = os.getenv("ACCOUNT_KEY")  # loaded from key.env
container_name = "test"
file_path = "sample.txt"

from azure.storage.blob import BlobServiceClient

connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

try:
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="sample.txt")
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"✅ File '{file_path}' uploaded to container '{container_name}'.")
except Exception as e:
    print(f"❌ Error: {e}")
