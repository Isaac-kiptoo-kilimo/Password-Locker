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

def display_accounts():
    
    return Account.display_accounts()

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
                break
        

if __name__=="__main__":
    main()