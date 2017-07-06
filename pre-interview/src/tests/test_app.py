import unittest
import flask
from src.app import app


class TestBucketListApp(unittest.TestCase):
    # def client(self):
    #     return src.app.test_client()

    def test_urls(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
