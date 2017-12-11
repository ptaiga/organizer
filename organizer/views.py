from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the organizer app index." )

def project(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

def task(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)