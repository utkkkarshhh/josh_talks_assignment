from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from service.models import Users, Tasks
from service.constants import ResponseMessages


class TaskCreateViewTest(APITestCase):

    def setUp(self):
        self.user = Users.objects.create(
            name="Test User",
            email="test@gmail.com"
        )

        self.valid_payload = {
            "name": "Test Task",
            "description": "Test Description",
            "task_type": "Test"
        }

        self.invalid_payload = {
            "name": "",
            "description": "",
            "task_type": "000"
        }

    def test_create_task_success(self):
        url = reverse('task_create_view', kwargs={'user_id': self.user.id})
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.TASK_CREATED.format(1))
        task = Tasks.objects.filter(creator=self.user).first()
        self.assertIsNotNone(task)
        self.assertEqual(task.name, self.valid_payload['name'])

    def test_create_task_invalid_data(self):
        url = reverse('task_create_view', kwargs={'user_id': self.user.id})
        response = self.client.post(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.INVALID_DATA)
        self.assertIn('errors', response.data)

    def test_create_task_invalid_user(self):
        url = reverse('task_create_view', kwargs={'user_id': 999})
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.USER_NOT_FOUND)

    def test_create_task_missing_fields(self):
        url = reverse('task_create_view', kwargs={'user_id': self.user.id})
        payload = {
            "name": "Test Task"
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.INVALID_DATA)
