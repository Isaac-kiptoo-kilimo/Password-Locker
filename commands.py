commands = [
    {
        "command": 'cu',
        "type": 'Users',
        "description": "To create a new user"
    },
    {
        "command": 'du',
        "type": 'Users',
        "description": "To delete a user"
    },
    {
        "command": 'lu',
        "type": 'Users',
        "description": "To list all users"
    },
    {
        "command": 'au',
        "type": 'Users',
        "description": "To authenticate a user"
    },
    {
        "command": 'aua',
        "type": 'Users',
        "description": "To Logout a user"
    },
    {
        "command": 'glu',
        "type": 'Users',
        "description": "To get the logged in user"
    },
    {
        "command": 'cc',
        "type": 'Credentials',
        "description": "To create a new credential"
    },
    {
        "command": 'lc',
        "type": 'Credentials',
        "description": "To List all credentials"
    },
    {
        "command": 'gluc',
        "type": 'Credentials',
        "description": "To List credentials for a logged in user"
    },
    {
        "command": 'dc',
        "type": 'Credentials',
        "description": "To delete a credential"
    },
    {
        "command": 'nc',
        "type": 'App',
        "description": "To make a new command"
    },
    {
        "command": 'h',
        "type": 'App',
        "description": "To get help"
    },
    {
        "command": 'q',
        "type": 'App',
        "description": "To Exit the app"
    },
]

def getCommand(command_):
    for command in commands:
        if command["command"] == command_:
            return command
    return None