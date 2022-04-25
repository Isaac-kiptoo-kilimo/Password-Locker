
import unittest
# from details import Account
from users import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user=User("1","Isaac kiptoo","isoo","isaac@gmail.com","111100")


    def test_init(self):
        self.assertEqual(self.new_user.id,"1")
        self.assertEqual(self.new_user.fullname,"Isaac kiptoo")
        self.assertEqual(self.new_user.username,"isoo")
        self.assertEqual(self.new_user.email,"isaac@gmail.com")
        self.assertEqual(self.new_user.password,"111100")


    def test_saveUser(self):
        self.new_user.saveUser() # saving the new user
        self.assertEqual(len(User.users),1)
        

    def tearDown(self):
        User.users=[]
    

    def test_deleteUser(self):
        self.new_user.saveUser()
        test_user=User("1","user","user_","test@user.com","0712345678",)
        test_user.saveUser()
        self.new_user.deleteUser()
        self.assertEqual(len(User.users),1)

    def test_listUsers(self):
        self.assertEqual(User.listUsers(),User.users)


if __name__=="__main__":
    unittest.main()