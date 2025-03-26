from rest_framework import serializers

class TaskAssignSerializer(serializers.Serializer):
    task_ids = serializers.ListField(
        child = serializers.IntegerField(min_value = 1),
        allow_empty = False,
        required = True
    )
