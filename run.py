#!/usr/bin/python3.8

import email
# from details import Account
from users import User
from credentials import Credentials


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
        password = input("Enter password:   ")
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
    max_len = 40
    id_rem_chars = 20 - len('id')
    user_rem_chars = 20 - len('User')
    platform_rem_chars = max_len - len('Platform')
    pass_rem_chars = max_len - len('Password')

    print("\n")
    print(title)
    print(f"{'ID'}" + " " * id_rem_chars,
          f"{'User'}" + " " * user_rem_chars,
          f"{'Platform'}" + " " * platform_rem_chars,
          f"{'Password'}" + " " * pass_rem_chars
          )
    print("-" * 120)
    for cred in creds:
        cred_id_rem_chars = 20 - len(str(cred['id']))
        cred_u_rem_chars = 20 - len(str(cred['user']))
        cred_p_rem_chars = max_len - len(cred['platform'])
        cred_pass_rem_chars = max_len - len(cred['password'])

        print(f"{cred['id']}" + " " * cred_id_rem_chars,
              f"{cred['user']}" + " " * cred_u_rem_chars,
              f"{cred['platform']}" + " " * cred_p_rem_chars,
              f"{cred['password']}" + " " * cred_pass_rem_chars,
              )

        print("-" * 120)

    print("\n")

def save_accounts(account):
    '''
    Function to save the new account
    '''
    account.save_account()

def deleteUser():
    user_id = input("Enter id of user you want to delete:     ")
    res = User.deleteUser(user_id)
    if res["statusCode"] == 200:
        print("User deleted successfully")
    else:
        print("Couldn't delete the user, maybe the user does not exist to delete.")

    '''
    Function to delete an account
    '''
    account.delete_account()

def listUsers():
    max_len = 30
    id_rem_chars = 10 - len('id')
    fname_rem_chars = max_len - len('Fullname')
    username_rem_chars = max_len - len('Fullname')
    email_rem_chars = max_len - len('Fullname')
    password_rem_chars = max_len - len('Fullname')

    users = User.users
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

    
    return Account.display_accounts()

def loginUser():
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



def find_account(username):
  
    return Account.find_by_username(username)

def check_existing_accounts(username):
    
    return Account.account_exist(username)

print()
print('PASSWORD LOCKER APPLICATION')
print("")

def main():
    print("Hello welcome,Enter your name to create an account")
    user_name=input()
    print(f"Hello {user_name}. what would you like to do?")
    print("\n")

    while True:
        print("Use these short codes : ca - create a new account,gp -generate new password ,cpg - get generated password by computor, da - display accounts,dp -display old password, fa -find an account, ex -exit the account list ")
        
        short_code=input().lower()
        if short_code== 'ca':
            print('New Account')
            print('-'*15)

            print('First Name....')
            f_name=input()

            print("Last Name....")
            l_name=input()

            print("Username ....")
            username_=input()

            print("Email ....")
            email_=input()

            print("Password ....")
            password_=input()

            save_accounts(create_account(f_name,l_name,username_,email_,password_)) # create and save new account.
            print ('\n')
            print(f"New account {f_name} {l_name} created")
            print ('\n')

        elif short_code=="da":
            if display_accounts():
                print("Here is the list of all your accounts..")
                print("\n")

                for account in display_accounts():
                     print(f"{account.first_name} {account.last_name}{account.email} ...{account.username}")
                     print('\n')

            else:
                print('\n')
                print("You dont seem to have any accounts yet")
                print('\n')

        elif short_code=="fa":
            print("Enter the username you want to search")
            search_username=input()

            if check_existing_accounts(search_username):
                search_account = find_account(search_username)
                print(f"{search_account.first_name} {search_account.last_name}")
                print('-' * 20)

                print(f"Username.......{search_account.username}")
                print(f"Email address.......{search_account.email}")

            else:
                print("That contact does not exist")

        elif short_code=="ex":
            print("Thank you,byee.....")
            break
        
        else:
            print("I really didn't get that. Please use the short codes")


if __name__=="__main__":
    main()