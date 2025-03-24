from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.models import Tasks, Users
from service.serializers import TaskCreateSerializer


class TaskCreateView(APIView):
    def post(self, request, user_id: int):
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return Response({
                'success': False,
                'message': ResponseMessages.USER_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskCreateSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': ResponseMessages.INVALID_DATA,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
        task = self._create_task(user, serializer.validated_data)

        return Response({
            'success': True,
            'message': ResponseMessages.TASK_CREATED.format(task.id),
        }, status=status.HTTP_201_CREATED)

    def _create_task(self, user_id, data):
        task = Tasks.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            task_type=data.get('task_type', ''),
            creator=user_id
        )
        task.save()
        return task
