#!/usr/bin/python3.8

# import email
# from details import Account
import random
from users import User
from credentials import Credentials
from commands import commands, getCommand
import uuid

# chars="abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ123456789!@#$&"


def printCommands():
    '''
    printCommands method is to enable the user navigate around the application
    '''
    print("Enter the following commands to use this app. ")
    for index, command in enumerate(commands):
        print(f"{index + 1}.", f"\'{command['command']}\'", f"{command['type']} - {command['description']}")
    print("\n\nGET STARTED.")

def createUser():
    fullname = input("Enter fullname:   ")
    username = input("Enter username:   ")
    email = input("Enter email:     ")
    password = input("Enter password:   ")
    res = User.createUser({
        "username": username,
        "fullname": fullname,
        "email": email,
        "password": password
    })
    if res["statusCode"] == 201:
        print(f"User created successfully with id -> {res['data']['id']}")

def createCredential():
    res = User.getLoggedInUser()
    if res["statusCode"] == 200:
        print(f"Creating new credentials for {res['data']['fullname']}")
        platform = input("Enter platform:   ")
        password_len=int(10)
        gen_pass=str(uuid.uuid4())[:8]
        password=""
        # for x in range(0,password_len):
            # password_char=random.choice(chars)
            # gen_pass=gen_pass + password_char
        # print("Here is your password:",password)
        print("choose password option")
        
        print("1.Enter your own password")
        print("2.Let the sytem choose for you")
        p_=input("Enter option;     ")
        if p_=="":
            print("Enter a valid option")
            p_=input("Enter option;     ")
        
        if p_=="1":
            password=input(f"Enter password:   ")
        elif p_=="2":
            password=gen_pass
        res = Credentials.createCredential({
        "user": res['data']['id'],
        "platform": platform,
        "password": password
        })

        if res["statusCode"] == 201:
            print(f"Credential created successfully with id -> {res['data']['id']}")
    else:
        print("We can't create create credentials for a non logged in user")

def tabulariseCredentials(title, creds):
    '''
    tabularising the credentials of the credentials object
    '''
    max_len = 20
    id_rem_chars = 10 - len('id')
    user_rem_chars = 10 - len('User')
    platform_rem_chars = max_len - len('Platform')
    pass_rem_chars = max_len - len('Password')

    print("\n")
    print(title)
    print(f"{'ID'}" + " " * id_rem_chars,
          f"{'User'}" + " " * user_rem_chars,
          f"{'Platform'}" + " " * platform_rem_chars,
          f"{'Password'}" + " " * pass_rem_chars
          )
    print("-" * 80)
    for cred in creds:
        cred_id_rem_chars = 10 - len(str(cred['id']))
        cred_u_rem_chars = 10 - len(str(cred['user']))
        cred_p_rem_chars = max_len - len(cred['platform'])
        cred_pass_rem_chars = max_len - len(cred['password'])

        print(f"{cred['id']}" + " " * cred_id_rem_chars,
              f"{cred['user']}" + " " * cred_u_rem_chars,
              f"{cred['platform']}" + " " * cred_p_rem_chars,
              f"{cred['password']}" + " " * cred_pass_rem_chars,
              )

        print("-" * 80)

    print("\n")

# def save_accounts(account):
#     '''
#     Function to save the new account
#     '''
#     account.save_account()

def deleteUser():
    '''
    Function to delete user
    '''
    user_id = input("Enter id of user you want to delete:     ")
    res = User.deleteUser(user_id)
    if res["statusCode"] == 200:
        print("User deleted successfully")
    else:
        print("Couldn't delete the user, maybe the user does not exist to delete.")   

def listUsers():
    '''
    getting all users list and user object
    '''
    max_len = 30
    id_rem_chars = 10 - len('id')
    fname_rem_chars = max_len - len('Fullname')
    username_rem_chars = max_len - len('Fullname')
    email_rem_chars = max_len - len('Fullname')
    password_rem_chars = max_len - len('Fullname')

    users = User.users
    '''
    list of users retrived.
    '''
    print("\n")
    print("A list of users within the database")
    print(f"{'ID'}" + " " * id_rem_chars,
          f"{'Fullname'}" + " " * fname_rem_chars,
          f"{'Username'}" + " " * username_rem_chars,
          f"{'Email'}" + " " * email_rem_chars,
          f"{'Password'}" + " " * password_rem_chars
          )
    print("-" * 120)
    for user in users:
        user_id_rem_chars = 10 - len(str(user['id']))
        user_f_rem_chars = max_len - len(user['fullname'])
        user_u_rem_chars = max_len - len(user['username'])
        user_e_rem_chars = max_len - len(user['email'])
        user_p_rem_chars = max_len - len(user['password'])

        print(f"{user['id']}" + " " * user_id_rem_chars,
              f"{user['fullname']}" + " " * user_f_rem_chars,
              f"{user['username']}" + " " * user_u_rem_chars,
              f"{user['email']}" + " " * user_e_rem_chars,
              f"{user['password']}" + " " * user_p_rem_chars
              )

        print("-" * 120)

    print("\n")


def loginUser():
    '''
    creating a user login function.
    '''
    print("\nWelcome to the login page.\nEnter your login details to get authenticated.")
    username = input("Enter your username:      ")
    password = input("Enter your password:      ")

    res = User.authenticateUser(
        {
            "username": username,
            "password": password
        }
    )

    if res["statusCode"] == 200:
        print(res["message"])
    else:
        print(res["message"])

def logoutUser():
    res = User.unAuthenticateUser()
    print(res["message"])


def getLoggedInUser():
    '''
    getLoggedInUser method is to retrive list of logged in users
    '''
    res = User.getLoggedInUser()
    if res["statusCode"] == 200:
        print2emptylines()
        print("The logged in user is: ")
        user = res["data"]
        print(f"Fullname:     {user['fullname']}")
        print(f"Username:     {user['username']}")
        print(f"Email:        {user['email']}")
        print(f"Password:     {user['password']}")
        print2emptylines()
    else:
        print(res["message"])


def listAllCredentials():
    tabulariseCredentials("All Credentials", Credentials.credentials)


def listLoggedInUserCredentials():
    '''
    creating a list of logged in user credentials in a simple table
    '''
    res = User.getCredentials()
    if res["statusCode"] == 200:
        tabulariseCredentials("All Credentials", res["data"])
    else:
        print(res["message"])


def deleteCredential():
    '''
    deleting credentials which you have stored.
    '''
    cred_id = input("Enter id of the credential you want to delete:     ")
    res = Credentials.deleteCredential(cred_id)
    print(res["message"])


def print2emptylines():
    print("\n")


print()
print('PASSWORD LOCKER APPLICATION')
print("")

def main():
    running = True
    printCommands()
    command = input("\nEnter command to continue:    ")
    # print("Hello welcome,Enter your name to create an account")
    # user_name=input()
    # print(f"Hello {user_name}. what would you like to do?")
    # print("\n")

    while running:
        com = getCommand(command)
        if com:
            if command == 'nc':
                command = input("Enter command to continue:    ")

            elif command == 'cu':
                createUser()

            elif command == 'lu':
                listUsers()

            elif command == 'du':
                deleteUser()

            elif command == 'au':
                loginUser()

            elif command == 'aua':
                logoutUser()

            elif command == 'glu':
                getLoggedInUser()

            elif command == 'lc':
                listAllCredentials()

            elif command == 'gluc':
                listLoggedInUserCredentials()

            elif command == 'cc':
                createCredential()

            elif command == 'dc':
                deleteCredential()

            elif command == 'h':
                printCommands()

            elif command == 'q':
                running = False
                break
            else:
                print("Command not found")

            command = input("\nType command to continue:    ")
        else:
            print("Command not found. Type 'h' to get help")
            command = input("\nEnter a valid command to continue:    ")

if __name__=="__main__":
    main()