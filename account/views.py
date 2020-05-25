from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Account
from main.cron import send_message


def index(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'account/index.html', {
        'num_rand_tasks': user.account.num_rand_tasks,
        'daily_email': user.account.daily_email,
        })

def save_changes(request):
    user = request.user if request.user.is_authenticated else None
    user_name = request.POST['user_name']
    user_email = request.POST['user_email']
    user.username = user_name
    user.email = user_email
    user.save()

    daily_email = True if 'daily_email' in request.POST else False
    num_rand_tasks = request.POST['num_rand_tasks']
    account = get_object_or_404(Account, user=user)
    account.daily_email = daily_email
    account.num_rand_tasks = int(num_rand_tasks) if int(num_rand_tasks) >= 0 else 0
    account.save()

    return HttpResponseRedirect(reverse('account:index'))

def send_daily_mail(request):
    user = request.user if request.user.is_authenticated else None
    send_message(user, check_account=False)
    return HttpResponse("Daily message has been sent!")
