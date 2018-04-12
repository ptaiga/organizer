from django.utils import timezone
from datetime import timedelta

from .models import Project, Task

def get_project_list(user, done_flag=False):
    return \
        Project.objects.filter(
            user=user,
            pub_date__lte=timezone.now(),
            done_flag=done_flag
        ).order_by('-pub_date')

def get_task_list(user, project, done_flag=False):
    return \
        Task.objects.filter(
            user=user,
            project=project,
            done_flag=done_flag
        )

def get_today_tasks(user):
    return \
        Task.objects.filter(
            user=user,
            done_flag=False,
            due_date__date__lte = timezone.now()
        )

def get_week_tasks(user):
    now = timezone.now()
    days_to_sunday = 6 - now.weekday()
    sunday = now + timedelta(days=days_to_sunday)
    return \
        Task.objects.filter(
            user=user,
            done_flag=False,
            due_date__date__lte = sunday
        )
