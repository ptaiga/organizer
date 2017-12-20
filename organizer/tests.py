from django.test import TestCase

import datetime
from django.utils import timezone

from .models import Task

class TaskModelTests(TestCase):
    def test_was_published_resently_with_future_task(self):
        """
        was_published_recently() return False for tasks whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_task = Task(pub_date=time)

        self.assertIs(future_task.was_published_recently(), False)

    def test_was_published_recently_with_old_task(self):
        """
        was_published_recently() returns False for tasks whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_task = Task(pub_date=time)
        self.assertIs(old_task.was_published_recently(), False)

    def test_was_published_recently_with_recent_task(self):
        """
        was_published_recently() returns True for tasks whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_task = Task(pub_date=time)
        self.assertIs(recent_task.was_published_recently(), True)