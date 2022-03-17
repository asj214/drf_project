from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):

    def setUp(self) -> None:
        self.data = {
            'email': 'hello123@abc.com',
            'name': 'hello123',
            'password': 'rewq1234'
        }

    def test_authenticated(self):
        url = '/api/auth/register'

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = '/api/auth/login'
        data = {
            'email': self.data.get('email'),
            'password': self.data.get('password')
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.data.get('token')

        url = '/api/auth/me'
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
