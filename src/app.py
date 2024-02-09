import boto3
from pprint import pprint
import json
import os
path = os.path.dirname(__file__)

client= boto3.client('secretsmanager')
print(path)
def create_secret(secret_name,user_id,password):
    response = client.create_secret(
        Name= secret_name,
        SecretString= f'{{"user_id":"{user_id}", "password" :"{password}"}}'
    )

def retrieve_secret(secret_name):
    response = client.get_secret_value(
    SecretId=secret_name
    )
    return response

def list_secrets():
    response = client.list_secrets()
    return [secret['Name'] for secret in response['SecretList']]

def delete_secret(secret_name):
    response=client.delete_secret(SecretId= secret_name)



def main():
    while True:
        response=input('Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it\n')
        if response== 'e':
            secret_identifier=input('Secret identifier:\n')
            user_id=input('UserId:\n')
            password=input('Password:\n')
            create_secret(secret_identifier,user_id,password)
            print('Secret has been saved')
        elif response =='r':
            secrets_list = list_secrets()
            secret_name = input('Specify secret to retrieve:\n')
            if secret_name in secrets_list:
                secret = retrieve_secret(secret_name)['SecretString']
                secret_dict = json.loads(secret)
                with open(f'{path}/../{secret_name}-secret.txt', 'w') as file:
                    file.write(f'UserId: {secret_dict["user_id"]}\nPassword: {secret_dict["password"]}')
                print(f'Secret stored in local file {secret_name}-secret.txt')
            else:
                print('Secret does not exist')
        elif response == 'd':
            secrets_list = list_secrets()
            secret_name=input('Specify the secret to delete:\n')
            if secret_name in secrets_list:
                delete_secret(secret_name)
                print('Deleted')
            else:
                print('Secret does not exist')
        elif response == 'l':
            secrets_list = list_secrets()
            print(f'{len(secrets_list)} secret(s) available')
            for item in secrets_list :print(item)
        elif response == 'x':
            print('Thank you. Goodbye.')
            break 
        else:
            response=input('Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it\n')
            

main()