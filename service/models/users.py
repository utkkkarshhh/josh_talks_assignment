from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
