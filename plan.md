Main function
while loop 
    ask for input 
        
        if input == entry:
            ask secret_identifier
            ask for user_id
            ask for password
            create_secret(secret_user, secret_password)
            give response ->('secrect saved')
        elif input == retrieval:
            ask secret_name
            give response ->('secret location')
        elif input == deletion:
            ask secret_name_to_delete
            give response ->('deleted')
        elif input == listing:
            list_secrets_available
                if none:
                    give response 0 secrets available
                else 
                    give respons ->(  number secrets available)
                    list_secrets_names
        
        elif input 'exit':
            give response( Thank you. Goodbye)
            break
        
    
        else:
            give response(invalid input)



