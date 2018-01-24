from django.utils import timezone

from .models import Project, Task

def get_project_list(user, done_flag):
    return \
        Project.objects.filter(
            user=user,
            pub_date__lte=timezone.now(),
            done_flag=False
        ).order_by('-pub_date')

def get_task_list(user, project, done_flag):
    return \
        Task.objects.filter(
            user=user,
            project=project,
            done_flag=done_flag
        )