import boto3
from pprint import pprint
s3=boto3.client('s3')

bucket_name="my-boto-bucket-1707303588"
#s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})

#s3.upload_file('../file1.txt', bucket_name, 'boto/file1.txt')
#s3.upload_file('../file2.txt', bucket_name, 'boto/file2.txt')

#object_read_list=s3.list_objects_v2(Bucket=bucket_name)
#readable_list=[]
#if 'Contents' in object_read_list:
    #for file in object_read_list['Contents']:
     #   readable_list.append(file["Key"])
#pprint(readable_list)

#response= s3.get_object(Bucket=bucket_name, Key='boto/file1.txt')
#response_body_file1=response['Body'].read().decode('utf-8')
#pprint(response_body_file1)


#delete_response=s3.delete_objects(
   # Bucket=bucket_name,
   # Delete={
       # 'Objects': [
        #    {
             #   'Key': 'boto/file1.txt' 
           # },
           # {
            #    'Key': 'boto/file2.txt'
           # },
        #],

    #},
#)
#pprint(delete_response)

delete_bucket_response=s3.delete_bucket(Bucket=bucket_name)
#pprint(delete_bucket_response)

deleted_bucket=s3.list_buckets()
pprint(deleted_bucket)