# Test cases can be run with either of the following:
# python -m unittest discover
# nosetests -v --rednose --nologcapture

import os
import unittest
import server
import logging
from flask_api import status    # HTTP Status Codes
from StringIO import StringIO

UPLOAD_FOLDER = 'static/img'

######################################################################
#  T E S T   C A S E S
######################################################################
class TestServer(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		try:
			os.remove(os.path.join(UPLOAD_FOLDER, 'test.png'))
		except Exception:
			log = logging.getLogger('No file to remove.. continuing')

	@classmethod
	def tearDownClass(self):
		try:
			os.remove(os.path.join(UPLOAD_FOLDER, 'test.png'))
		except Exception:
			log = logging.getLogger('No file to remove.. continuing')

	def setUp(self):
		server.app.debug = True
		self.app = server.app.test_client()

	def test_get_form(self):
		log = logging.getLogger("Test GET form")
		resp = self.app.get('/')
		self.assertTrue('Upload new File' in resp.data)
		self.assertTrue(resp.status_code == status.HTTP_200_OK)

	def test_post_upload(self):
		log = logging.getLogger("Test POST upload")
		# grab test image
		with open(os.path.join(UPLOAD_FOLDER, 'newapp-icon.png')) as test:
			imgStringIO = StringIO(test.read())

		data=dict( {'file': (imgStringIO, 'test.png')} )
		resp = self.app.post('/', data=data, follow_redirects=True, content_type='multipart/form-data')
		self.assertTrue('Upload succesful', resp.data)

######################################################################
#   M A I N
######################################################################
if __name__ == '__main__':
	unittest.main()