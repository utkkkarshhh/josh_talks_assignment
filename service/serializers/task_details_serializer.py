from rest_framework import serializers
from service.models import Tasks

class TaskDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'name', 'description', 'status', 'created_at', 'updated_at']