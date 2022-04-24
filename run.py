#!/usr/bin/python3.8

import email
from details import Account


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


def save_accounts(account):
    '''
    Function to save the new account
    '''
    account.save_account()

def delete_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def display_accounts():
    
    return Account.display_accounts()

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