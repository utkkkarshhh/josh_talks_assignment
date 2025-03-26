from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from service.models import Users, Tasks
from service.constants import ResponseMessages


class TaskDetailsViewTest(APITestCase):

    def setUp(self):
        self.user = Users.objects.create(
            name="Test User",
            email="test@gmail.com"
        )

        self.task1 = Tasks.objects.create(
            name="Test Task 1",
            description="Test Description 1",
            creator=self.user
        )

        self.task2 = Tasks.objects.create(
            name="Test Task 2",
            description="Test Description 2",
            creator=self.user
        )

        self.task1.users.add(self.user)
        self.task2.users.add(self.user)

    def test_get_tasks_success(self):
        url = reverse('task_details_view', kwargs={'user_id': self.user.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.TASKS_FETCHED_SUCCESSFULLY)
        data = response.data.get('data')
        self.assertEqual(len(data), 2)
        task_names = [task.get('name') for task in data]
        self.assertIn(self.task1.name, task_names)
        self.assertIn(self.task2.name, task_names)

    def test_get_tasks_user_not_found(self):
        url = reverse('task_details_view', kwargs={'user_id': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.USER_NOT_FOUND)

    def test_get_tasks_no_assigned_tasks(self):
        new_user = Users.objects.create(
            name="New User",
            email="newuser@gmail.com"
        )
        url = reverse('task_details_view', kwargs={'user_id': new_user.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('success'))
        self.assertEqual(response.data.get('message'), ResponseMessages.TASKS_FETCHED_SUCCESSFULLY)
        data = response.data.get('data')
        self.assertEqual(len(data), 0)
