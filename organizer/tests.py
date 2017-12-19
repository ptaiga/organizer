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

