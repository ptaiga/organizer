from django.http import HttpResponse
from django.shortcuts import render

from .models import Task

def index(request):
    latest_task_list = Task.objects.order_by('-pub_date')[:5]
    context = {
        'latest_task_list': latest_task_list,    
	}
    return render(request, 'organizer/index.html', context)

def project(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

def task(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)