import boto3
from pprint import pprint
import json
client= boto3.client('secretsmanager')

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

# pprint(retrieve_secret()['SecretString'])

#create_secret("examplesecret7","user_id7","password7")

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
            secret_name = input('Specify secret to retrieve:\n')
            secret = retrieve_secret(secret_name)['SecretString']
            with open(f'{secret_name}-secret.txt', 'w') as file:
                file.write(secret)
            print(f'Secret stored in local file {secret_name}-secret.txt')
        elif response == 'd':
            print('deleted')
        elif response == 'l':
            print('list')
        elif response == 'x':
            print('Godbye')
            break 
        else:
            response=input('invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it\n')
            

main()