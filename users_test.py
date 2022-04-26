# import pyperclip
from cgi import test
from hashlib import new
import unittest

from keyring import get_credential

from users import User
from credentials import Credentials

class UserTest(unittest.TestCase):
    '''
    Test class that defines test cases for the user and credentials class behaviours.

    Unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user=User("1","Isaac kiptoo","isoo","isaac@gmail.com","111100")
   

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.id,"1")
        self.assertEqual(self.new_user.fullname,"Isaac kiptoo")
        self.assertEqual(self.new_user.username,"isoo")
        self.assertEqual(self.new_user.email,"isaac@gmail.com")
        self.assertEqual(self.new_user.password,"111100")


    def test_saveUser(self):
        '''
        test_saveUser test case to test if the user object is saved into
         the users
        '''
        self.new_user.saveUser() # saving the new user
        self.assertEqual(len(User.users),1)
        
    def test_createUser(self):
        '''
        test_createUser test case to test if the user object is created and appended into
         the users
        '''
        self.new_user.createUser
        self.assertEqual(len(User.users),0)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users=[]
    

    def test_deleteUser(self):
        '''
        test_deleteUser to test if we can remove a user from our users list
        '''
        self.test_user=User
        self.test_user.getUser("user_id")
        self.new_user.deleteUser("user_id")
        
        self.assertEqual(len(User.users),0)

    def test_getLoggedInUser(self):
        test_new_credentials= Credentials() # 
        test_new_credentials.createCredential(Credentials)

        get_credential = Credentials.get_by_id()

        self.assertEqual(get_credential.id,test_new_credentials.id)
    
    def test_authenticateUser(self):
        self.username="isaac"
        self.password="password"
        self.new_test_user=self.password + self.username
        self.new_user_logged=self.authenticateUser(Credentials)
        
        self.assertEqual(self.new_test_user,self.new_user_logged)
    
    def test_createCredentials(self):
        self.test_new_credentials=Credentials.createCredential('credential')
        self.credentials=Credentials.credentials.append()
        self.assertEqual(len(self.test_new_credentials),2)

    
    def test_deleteCredentials(self):
        '''
        test_deleteUser to test if we can remove a user from our users list
        '''
        self.test_credential=Credentials
        # self.test_credential.res
        self.test_new_credentials=Credentials.deleteCredential(1)
        
        self.assertEqual(len(Credentials.credentials),1)
    
    def test_getUserCredentials(self):
        # self.new_getUserCredential=Credentials.createCredential('credential')
        # test_new_credentials= Credentials.getCredential(1) 
        # test_new_credentials.createCredential()

        get_credential = Credentials.getCredential(1)

        self.assertEqual(len(get_credential),3)

if __name__=="__main__":
    unittest.main()