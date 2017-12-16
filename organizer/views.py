from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Project, Task

def index(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,    
	}
    return render(request, 'organizer/index.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'organizer/project.html', {'project': project})
	
def task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'organizer/task.html', {'task': task})
	# return HttpResponse("You're looking at task %s." % task_id)