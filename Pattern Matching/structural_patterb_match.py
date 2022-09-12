"""def execute_command(command):
    if command == "ls":
        print(' $ listing files')
    elif command == 'cd':
        print("$ changing directory")
    else:
        print('$ command not implemented')
    
    print('...rest 0f the code')


execute_command('ls')"""

def execute_command(command: str):
    match command:
        case "ls":
            print(' $ listing files')
        case 'cd':
            print("$ changing directory")
        case _:
            print('$ command not implemented')
    
    print('...rest 0f the code')


execute_command('ls')