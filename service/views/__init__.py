__all__ = [
    "HealthCheck",
    "TaskAssignView",
    "TaskCreateView",
    "TaskDetailsView",
]

from service.views.healthcheck import HealthCheck
from service.views.task_assign_view import TaskAssignView
from service.views.task_create_view import TaskCreateView
from service.views.task_details_view import TaskDetailsView
