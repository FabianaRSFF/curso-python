"""def execute_command(command):
    if command == "ls":
        print(' $ listing files')
    elif command == 'cd':
        print("$ changing directory")
    else:
        print('$ command not implemented')
    
    print('...rest 0f the code')


execute_command('ls')"""

'''def execute_command(command: str):
    match command:
        case "ls":
            print(' $ listing files')
        case 'cd':
            print("$ changing directory")
        case _:
            print('$ command not implemented')
    
    print('...rest 0f the code')


execute_command('ls')'''

def execute_command(command: str):
    match command.split():
        #case ["ls", path]:
            #print(' $ listing files from', path)
        case ["ls", *directories, '--force']:
            for directory in directories:
                print(' $ listing files Forced', directory)
        case ["ls", *directories]:
            for directory in directories:
                print(' $ listing files', directory)
        case ['cd', path1, path2, path3]:
            print("$ changing directory to", path1, path2, path3)
        case _:
            print('$ command not implemented')
    

execute_command('ls /home /users /ovni --force')
execute_command('ls /home /users /ovni')
execute_command('cd /home /users /etc')