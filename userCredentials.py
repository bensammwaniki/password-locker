from passlock import User
from passlock import Credentials
import unittest

class test_class(unittest.TestCase):
    

    def setUp(self):
        self.new_user = User('bnm','1234zxcvb')

    def test_init(self):
        self.assertEqual(self.new_user.username,'bnm')
        self.assertEqual(self.new_user.password,'1234zxcvb')
