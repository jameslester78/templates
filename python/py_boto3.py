import boto3
import json
import os





#fetch aws secret values from using Access and Secret Access Key stored in environent variables
#secretId = rdsCredentials, keys ['rdsUser','rdsPass']
#store key values in environment variables

botoClient = boto3.client('secretsmanager',aws_access_key_id=os.environ['awsAccessKeyID'],aws_secret_access_key=os.environ['awsSecretAccessKey'])
creds = json.loads (botoClient.get_secret_value(SecretId='rdsCredentials')['SecretString'])

for key,value in creds.items():
    if key == 'rdsUser': os.environ[key] = value
    if key == 'rdsPass': os.environ[key] = value







#download files from s3 to local storage
    
session = boto3.Session(
    aws_access_key_id=os.environ['awsAccessKeyID'],
    aws_secret_access_key=os.environ['awsSecretAccessKey'],
    )
    
s3 = session.resource('s3')  
bucket = s3.Bucket('bucketName')

for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()

    file = open('file.csv', 'w')
    file.write(body.decode("utf-8"))
    file.close()







#move files from unprocessed folder to processed folder
    
copy_source = {
    'Bucket': f'{sourceBucket}',
    'Key': f'{source}'
}    

session = boto3.Session(
    aws_access_key_id=os.environ['awsAccessKeyID'],
    aws_secret_access_key=os.environ['awsSecretAccessKey'],
)
    
s3 = session.resource('s3')
bucket = s3.Bucket(sourceBucket)

bucket.copy(copy_source, destination)
s3.Object(sourceBucket,source).delete()