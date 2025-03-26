from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.serializers import TaskAssignSerializer
from service.models import Tasks, Users

class TaskAssignView(APIView):
    def patch(self, request, user_id: int):
        user = Users.objects.filter(id=user_id).first()
        if not user:
            return Response({
                'success': False,
                'message': ResponseMessages.USER_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskAssignSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': ResponseMessages.INVALID_DATA,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
        task_ids = serializer.validated_data.get('task_ids')
        tasks = Tasks.objects.filter(id__in=task_ids)
        
        if len(tasks) != len(task_ids):
            invalid_ids = set(task_ids) - set(tasks.values_list('id', flat=True))
            return Response({
                'success': False,
                'message': ResponseMessages.TASK_WITH_IDS_NOT_FOUND.format(list(invalid_ids))
            }, status=status.HTTP_404_NOT_FOUND)
            
        for task in tasks:
            task.users.add(user)
            
        return Response({
            'success': True,
            'message': ResponseMessages.TASK_SUCCESSFULLY_ASSIGNED,
        }, status=status.HTTP_200_OK)
