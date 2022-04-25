# import pyperclip
import unittest

from users import User

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
        

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users=[]
    

    def test_deleteUser(self):
        '''
        test_deleteUser to test if we can remove a user from our users list
        '''
        user_id=1
        self.new_user.getUser(user_id)
        test_user=User("1","user","user_","test@user.com","0712345678",)
        test_user.getUser(user_id)
        self.new_user.deleteUser()
        self.assertEqual(len(User.users),1)

    # def test_listUsers(self):
    #     self.assertEqual(User.listUsers(),User.users)


if __name__=="__main__":
    unittest.main()