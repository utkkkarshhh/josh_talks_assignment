from django.db import models
from service.models import Users


class Tasks(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    task_type = models.CharField(max_length=50, blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    users = models.ManyToManyField(Users, related_name='assigned_tasks')
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='created_tasks')
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
