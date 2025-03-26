from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from service.constants import ResponseMessages
from service.models import Tasks, Users
from service.serializers import TaskDetailsSerializer


class TaskDetailsView(ListAPIView):
    serializer_class = TaskDetailsSerializer
    
    def get(self, request, user_id: int):
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return Response({
                'success': False,
                'message': ResponseMessages.USER_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        tasks = Tasks.objects.filter(users=user)
        serializer = self.get_serializer(tasks, many=True)
        
        return Response({
            'success': True,
            'message': ResponseMessages.TASKS_FETCHED_SUCCESSFULLY,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
