from rest_framework import serializers

class TaskCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=1000)
    task_type = serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
