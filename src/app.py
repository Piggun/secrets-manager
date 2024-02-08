import boto3
client= boto3.client('secretsmanager')

def create_secret(secret_name,user_id,password):
    response = client.create_secret(
        Name= secret_name,
        SecretString= f'{{"user_id":"{user_id}", "password" :"{password}"}}'
    )
 

#create_secret("examplesecret7","user_id7","password7")

def main():
    while True:
        response=input('Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it\n')
        if response== 'e':
            secret_identifier=input('Secret identifier:')
            user_id=input('UserId:')
            password=input('Password:')
            create_secret(secret_identifier,user_id,password)
            print('Secret has been saved')
        elif response =='r':
            print('retrieve')
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