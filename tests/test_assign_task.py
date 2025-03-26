from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from service.models import Users, Tasks
from service.constants import ResponseMessages


class TaskAssignViewTest(APITestCase):

    def setUp(self):
        self.user = Users.objects.create(
            name="Test User",
            email="test@gmail.com"
        )

        self.task1 = Tasks.objects.create(
            name="Test",
            description="Test",
            creator=self.user
        )

        self.task2 = Tasks.objects.create(
            name="Test",
            description="Test",
            creator=self.user
        )

        self.valid_payload = {
            "task_ids": [self.task1.id, self.task2.id]
        }

        self.invalid_payload = {
            "task_ids": [999, 1000]
        }

    def test_assign_tasks_success(self):
        url = reverse('task_assign_view', kwargs={'user_id': self.user.id})
        response = self.client.patch(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.TASK_SUCCESSFULLY_ASSIGNED)
        self.assertIn(self.user, self.task1.users.all())
        self.assertIn(self.user, self.task2.users.all())

    def test_assign_tasks_user_not_found(self):
        url = reverse('task_assign_view', kwargs={'user_id': 999})
        response = self.client.patch(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.USER_NOT_FOUND)

    def test_assign_tasks_invalid_payload(self):
        url = reverse('task_assign_view', kwargs={'user_id': self.user.id})
        response = self.client.patch(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.INVALID_DATA)

    def test_assign_tasks_not_found(self):
        url = reverse('task_assign_view', kwargs={'user_id': self.user.id})
        response = self.client.patch(url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.data.get('success'))
        self.assertIn('message', response.data)
