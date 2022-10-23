from rest_framework.test import APITestCase
from django.urls import reverse
from custom_users.models import MyUser as User
from tasks.models import ManageTask


class UserLogin(APITestCase):
    url_token = reverse("token_obtain_pair")
    list_task = reverse("tasks:list_task")

    def setUp(self):
        # Create test User
        self.user = User.objects.create_user(username="cefer", email="cefer.h2018@mail.ru", password="test12345")
        # User login
        self.client.login(username='cefer', password='test12345')
        # Create test Token
        response = self.client.post(self.url_token, {"username": "cefer", "password": "test12345"})
        self.token = response.data['access']
        self.assertEqual(200, response.status_code)
        # Keep the token in header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_task_list(self):
        # Create test ManageTask
        self.task = ManageTask(title="Test task", description="Test task", deadline='2022-11-23 16:36:39+00:00')
        self.task.save()
        self.task.user.add(self.user)
        # Test TaskList
        response = self.client.get(self.list_task)
        self.assertEqual(200, response.status_code)