import unittest
from app.models import Management
class ManagementTest (unittest.TestCase):
    '''
    Test class to test the behaviour of the Management class
    '''
    def setUp(self):
        '''
        Set up method that will return before ecah test
        '''
        self.new_comment =Management('Strike',"There will be no strike")
    def test_instance(self):
        self.assertTrue(isinstance)(self.new_comment,Management))