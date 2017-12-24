# Test cases can be run with either of the following:
# python -m unittest discover
# nosetests -v --rednose --nologcapture

import unittest
import server
import logging

######################################################################
#  T E S T   C A S E S
######################################################################
class TestServer(unittest.TestCase):
    def setUp(self):
        server.app.debug = True
        self.app = server.app.test_client()

    # toDo: come back and create a meaningful test
    def test_index(self):
        resp = self.app.get('/')
        self.assertTrue (True == True)

######################################################################
#   M A I N
######################################################################
if __name__ == '__main__':
    unittest.main()