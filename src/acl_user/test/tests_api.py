import json
from  django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .test_setup import TestSetUp


class ApiAclUsers(TestSetUp):

    def test_user_register(self):
        self.user = User.objects.create_superuser(username='test',
                                       email='testing@test.id',
                                       password='some-long-word-passwd')

        self.assertEqual(self.user.username,'test')
        self.assertEqual(self.user.email, 'testing@test.id')
        self.assertEqual(self.user.is_superuser, 1, 'Super User')
        self.assertEqual(self.user.is_active, 1, 'Active User')

    def api_authentication(self):
        self.user = User.objects.create_superuser(username='test',
                                                  email='testing@test.id',
                                                  password='some-long-word-passwd')
        url = reverse('token-auth')
        resp = self.client.post(url, {'username': 'test', 'password': 'some-long-word-passwd'}, format='json')
        self.token = resp.data['access']
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + format(self.token))

    def test_get_users(self):
        res = self.client.get(self.user_list, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_create(self):
        self.api_authentication()

        data = {
                "email": "testman@test.com",
                "first_name": "test",
                "last_name": "kingpin",
                "phone": "628837439490321",
                "active": False
        }
        response = self.client.post(self.user_create, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_by_id(self):
        self.api_authentication()

        data = {
            "email": "testman@test.com",
            "first_name": "test",
            "last_name": "kingpin",
            "phone": "628837439490321",
            "active": False
        }
        self.client.post(self.user_create, data, format='json')

        res = self.client.get('/api/users/testman@test.com/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        self.api_authentication()

        data = {
            "email": "testman@test.com",
            "first_name": "test",
            "last_name": "kingpin",
            "phone": "628837439490321",
            "active": False
        }
        self.client.post(self.user_create, data, format='json')

        res = self.client.patch(self.user_update,{'active':True})
        self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)

    def test_user_delete(self):
        self.api_authentication()

        data = {
            "email": "testman@test.com",
            "first_name": "test",
            "last_name": "kingpin",
            "phone": "628837439490321",
            "active": False
        }
        self.client.post(self.user_create, data, format='json')

        res = self.client.delete(self.user_delete, format='json')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


