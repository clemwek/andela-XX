import unittest
from src.app import app


class TestBucketListApp(unittest.TestCase):
    def register(self, email, password, name):
        client = app.test_client(self)
        return client.post(
            '/register',
            data=dict(inputEmail=email, inputPassword=password, inputName=name),
            follow_redirects=True
        )

    def login(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    def test_urls(self):
        client = app.test_client(self)
        welcome = client.get('/', content_type='html/text')
        self.assertEqual(welcome.status_code, 200)

        login = client.get('/login', content_type='html/text')
        self.assertEqual(login.status_code, 200)

        bucketlist = client.get('/bucketlist', content_type='html/text')
        # app.login('admin@test.com', 'admin')
        self.assertEqual(bucketlist.status_code, 302)

        add_bucketlist = client.get('/add_bucketlist', content_type='html/text')
        self.assertEqual(add_bucketlist.status_code, 302)

        # add_activity = client.get('/add_activity', content_type='html/text')
        # self.assertEqual(add_activity.status_code, 200)

    def test_register(self):
        # client = app.test_client(self)
        # data = {'inputName': 'john', 'inputEmail': 'test@test.com', 'inputPassword': 'test'}
        # response = client.post('register', data=data, follow_redirects=True)
        response = self.register('patkennedy79@gmail.com', 'FlaskIsAwesome', 'FlaskIsAwesome')
        # self.assertEqual(response.status_code, 200)
        self.assertIn(b'logged in', response.data)

if __name__ == '__main__':
    unittest.main()
