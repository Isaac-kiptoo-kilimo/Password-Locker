
import unittest
# from details import Account
from users import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_account=User("Isaac","limo","isoo","0721jk","isaac@gmail.com")


    def test_init(self):
        self.assertEqual(self.new_account.first_name,"Isaac")
        self.assertEqual(self.new_account.last_name,"limo")
        self.assertEqual(self.new_account.username,"isoo")
        self.assertEqual(self.new_account.password,"0721jk")
        self.assertEqual(self.new_account.email,"isaac@gmail.com")
    def test_save_account(self):
        self.new_account.save_account() # saving the new contact
        self.assertEqual(len(User.account_list),1)
        # print(Detail.account_list)

    def tearDown(self):
        User.account_list=[]
    
    def test_save_multiple_account(self):
        self.new_account.save_account()
        test_account=User("Test","user","user_","0712345678","test@user.com")
        test_account.save_account()
        self.assertEqual(len(User.account_list),2)


    def test_delete_account(self):
        self.new_account.save_account()
        test_account=User("Test","user","user_","0712345678","test@user.com")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(User.account_list),1)

    def test_display_account(self):
        self.assertEqual(User.display_accounts(),User.account_list)


if __name__=="__main__":
    unittest.main()