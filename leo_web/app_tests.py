import os
import app
import unittest
import tempfile
import json

class LeoTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_json_content_type(self):
        resp = self.app.get('/0')
        assert('application/json' in resp.content_type)

    def test_valid_json_response(self):
        resp = self.app.get('/0')
        data = json.loads(resp.data)
        assert(isinstance(data, dict))

    def test_negative_request(self):
        resp = self.app.get('/-1')
        data = json.loads(resp.data)
        assert(data.has_key('error') == True)

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
