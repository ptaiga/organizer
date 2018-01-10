import datetime

from django.db import models
from django.utils import timezone

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    done_flag = models.BooleanField(default=False)
    def __str__(self):
	    return self.project_name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
        default=None, null=True)
    task_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    done_flag = models.BooleanField(default=False)
    def __str__(self):
	    return self.task_name
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'