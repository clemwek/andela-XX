import unittest
import flask
from src.app import app


class TestBucketListApp(unittest.TestCase):
    # def client(self):
    #     return src.app.test_client()

    def test_urls(self):
        client = app.test_client(self)
        welcome = client.get('/', content_type='html/text')
        self.assertEqual(welcome.status_code, 200)

        login = client.get('/login', content_type='html/text')
        self.assertEqual(login.status_code, 200)

        bucketlist = client.get('/bucketlist', content_type='html/text')
        self.assertEqual(bucketlist.status_code, 200)

        add_bucketlist = client.get('/add_bucketlist', content_type='html/text')
        self.assertEqual(add_bucketlist.status_code, 200)

        add_activity = client.get('/add_activity', content_type='html/text')
        self.assertEqual(add_activity.status_code, 200)

if __name__ == '__main__':
    unittest.main()
