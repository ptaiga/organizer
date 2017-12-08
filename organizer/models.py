import datetime

from django.db import models
from django.utils import timezone

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
	    return self.project_name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
	    return self.task_name
    def was_published_recently(self):
	    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)