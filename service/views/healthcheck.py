from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessages


class HealthCheck(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'success': True,
            'message': ResponseMessages.HEALTHY_SERVICE
        }, status=status.HTTP_200_OK)
