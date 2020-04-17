from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Account


def index(request):
    user = request.user if request.user.is_authenticated else None
    num_rand_tasks = user.account.num_rand_tasks
    return render(request, 'account/index.html', {
        'num_rand_tasks': num_rand_tasks
        })

def save_changes(request):
    user = request.user if request.user.is_authenticated else None
    user_name = request.POST['user_name']
    num_rand_tasks = request.POST['num_rand_tasks']
    account = get_object_or_404(Account, user=user)
    account.user.username = user_name
    account.num_rand_tasks = int(num_rand_tasks) if int(num_rand_tasks) >= 0 else 0
    account.save()
    return HttpResponseRedirect(reverse('account:index'))
