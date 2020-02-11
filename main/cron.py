#!/usr/bin/python3.6

import sys, os

sys.path.append('/home/ptaiga/main/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from django.urls import reverse

from main.private_settings import email_to, email_from, \
                                    email_auth_user, email_auth_password

from organizer.models import Task


def send(email_to, subject, content):
    if send_mail(subject, content, email_from, [email_to],
        fail_silently=False, auth_user=email_auth_user,
        auth_password=email_auth_password
    ):
        print(f"Email to '{email_to}' send")
        return True
    else:
        print("Email to '{email_to}' doesn't send. Try again later")
        return False


def task():
    for user in User.objects.all():
        if not user.email: continue
        tasks = Task.objects.filter(user=user,
                                    done_flag=False,
                                    project__done_flag=False,
                                    due_date__date__lte=timezone.now())
        if not tasks: continue
        subject = f"{user.username.capitalize()}, tasks for {timezone.now().date()}"
        content = f"{timezone.now().date()}:\n\n"
        for task in tasks:
            content += f" - {task.task_name}\n"

        content += "\nKeep making your dream come true step by step:"
        content += f"\nhttps://ptaiga.pythonanywhere.com{reverse('organizer:index')}\n"
        # content += f"\nhttps://ptaiga.pythonanywhere.com{reverse('organizer:show', args=('today',))}"

        inbox_tasks = Task.objects.filter(user=user,
                                          done_flag=False,
                                          project=None)
        if inbox_tasks:
            content += "\nInbox:\n"
            for task in inbox_tasks:
                content += f" - {task.task_name}"
                content += f" ({task.due_date.date()})\n" if task.due_date else "\n"

        random_tasks = Task.objects.filter(user=user,
                                           done_flag=False,
                                           project__done_flag=False,
                                           due_date=None).order_by('?')[:1]
        if random_tasks:
            content += f"\nRandom:\n"
            for task in random_tasks:
                content += f" - {task.task_name}"
                content += f" (https://ptaiga.pythonanywhere.com{reverse('organizer:task', args=(task.id,))})\n"

        content += "\n\n--\nHave a productive day!\nYour Organizer\n"
        send(user.email, subject, content) # print(content)


if __name__ == "__main__":
    task()
