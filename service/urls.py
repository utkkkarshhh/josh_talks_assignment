from django.urls import path

from service.views import *

urlpatterns = [
    path('healthcheck', HealthCheck.as_view(), name='healthcheck'),
    path('task/create/<int:user_id>', TaskCreateView.as_view(), name='task_create_view'),
    path('task/list/<int:user_id>', TaskListingView.as_view(), name='task_listing_view'),
    path('task/assign/<int:user_id>', TaskAssignView.as_view(), name='task_assign_view'),
]
