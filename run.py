#!/usr/bin/python3.8


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

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def main():
    print("Hello enter you Details to create an account")

if __name__=="__main__":
    main()