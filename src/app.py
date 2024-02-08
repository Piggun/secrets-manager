def main():
    while True:
        response=input('Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it\n')
        if response== 'e':
            print(response)
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