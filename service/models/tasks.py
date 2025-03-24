from django.db import models


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
    users = models.ManyToManyField('users', related_name='tasks')
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
