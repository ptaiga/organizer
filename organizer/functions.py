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

def get_task_list(user, project, done_flag=False, status=None):
    if status == 'today':
        return \
            Task.objects.filter(
                user=user,
                done_flag=False,
                due_date__date__lte = timezone.now()
            ).exclude(snooze_date__date=timezone.now().date())
    elif status == 'week':
        now = timezone.now()
        days_to_sunday = 6 - now.weekday()
        sunday = now + timedelta(days=days_to_sunday)
        return \
            Task.objects.filter(
                user=user,
                done_flag=False,
                due_date__date__lte = sunday
            ).exclude(snooze_date__date=timezone.now().date())

    return \
        Task.objects.filter(
            user=user,
            project=project,
            done_flag=done_flag
        ).exclude(snooze_date__date=timezone.now().date())

def get_task_count(user):
    num_inbox_tasks = Task.objects.filter(
            user=user,
            project=None,
            done_flag=False
        ).exclude(snooze_date__date=timezone.now().date()).count()
    num_today_tasks = Task.objects.filter(
            user=user,
            done_flag=False,
            due_date__date__lte = timezone.now()
        ).exclude(snooze_date__date=timezone.now().date()).count()

    now = timezone.now()
    days_to_sunday = 6 - now.weekday()
    sunday = now + timedelta(days=days_to_sunday)
    num_week_tasks = Task.objects.filter(
            user=user,
            done_flag=False,
            due_date__date__lte = sunday
        ).exclude(snooze_date__date=timezone.now().date()).count()

    return num_inbox_tasks, num_today_tasks, num_week_tasks
