#!/usr/bin/python3.8


import email
from details import Account


def create_account(fname,lname,username,password,email):
    '''
    Function to create a new account
    '''
    new_account =Account(fname,lname,username,password,email)
    return new_account

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
            username=input()

            print("Email ....")
            email=input()

            print("Password ....")
            password=input()

        break
        

if __name__=="__main__":
    main()