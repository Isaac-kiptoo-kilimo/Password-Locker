
import unittest
from details import Details

class DetailsTest(unittest.TestCase):

    def setUp(self):
        self.new_account=Details("Isaac","limo","isoo","0721jk","isaac@gmail.com")


    def test_init(self):
        self.assertEqual(self.new_account.first_name,"Isaac")
        self.assertEqual(self.new_account.last_name,"limo")
        self.assertEqual(self.new_account.username,"isoo")
        self.assertEqual(self.new_account.password,"0721jk")
        self.assertEqual(self.new_account.email,"isaac@gmail.com")

if __name__=="__main__":
    unittest.main()