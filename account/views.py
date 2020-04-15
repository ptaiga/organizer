from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    user = request.user if request.user.is_authenticated else None
    num_rand_tasks = user.account.num_rand_tasks #1
    return render(request, 'account/index.html', {
        'num_rand_tasks': num_rand_tasks
        })
    # return HttpResponse(f"{request.user}, it's your account!")
