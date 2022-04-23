import unittest

class Account:

    account_list=[]
    def __init__(self,first_name,last_name,username,      
                 password,email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.password=password
        self.email=email

    def save_account(self):
        self.account_list.append(self)


    def delete_account(self):
        self.account_list.remove(self)

    @classmethod
    def display_accounts(cls):
        return cls.account_list

