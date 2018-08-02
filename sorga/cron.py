#!/usr/bin/python3.6

import sys, os

sys.path.append('/home/ptaiga/sorga/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sorga.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth.models import User
from django.core.mail import send_mail

from sorga.private_settings import email_to, email_from, \
                                    email_auth_user, email_auth_password

def task():
    if send_mail(
        '[Organizer] Today tasks',
        "Your today tasks:",
        email_from,
        ['ptaiga@gmail.com'],
        fail_silently=False,
        auth_user=email_auth_user,
        auth_password=email_auth_password
    ):
        print("Email send")
        return
    else:
        print("Email doesn't send. Try again later")
        return

if __name__ == "__main__":
    task()
