# Importando bibliotecas
import boto3  # Python SDK
import os

# inicializa Simple Storage Service
s3_client = boto3.client("s3", region_name='sa-east-1')

# cria bucket
s3_client.create_bucket(
    Bucket='indicium-challenge',
    CreateBucketConfiguration={
        'LocationConstraint': 'sa-east-1'
    }
)

# uploading arquivos
for root, dirs, files in os.walk('..\Solutions\data'):
    for file in files:
        s3C.upload_file(os.path.join(root, file), 'indicium-challenge', file)

exit()
