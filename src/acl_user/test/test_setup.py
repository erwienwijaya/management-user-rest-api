from django.urls import reverse
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    def setUp(self):
        self.user_list = reverse('users:user-list')
        self.user_create = reverse('users:user-create')
        self.user_update = reverse('users:user-update',kwargs={'email':'testman@test.com'})
        self.user_delete = reverse('users:user-delete',kwargs={'email':'testman@test.com'})

        return super().setUp()

    def tearDown(self):
        return super().tearDown()