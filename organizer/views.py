from django.http import HttpResponse

from .models import Task

def index(request):
    latest_task_list = Task.objects.order_by('-pub_date')[:5]
    output = ', '.join([t.task_name for t in latest_task_list])
    return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the organizer app index." )

def project(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

def task(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)