from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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

def choice(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    try:
        selected_task = project.task_set.get(pk=request.POST['task'])
    except (KeyError, Task.DoesNotExist):
        return render(request, 'organizer/project.html', {
            'project': project,
            'error_message': "You didn't select a task."
        })
    else:
        return HttpResponseRedirect(reverse('organizer:task', 
            args=(selected_task.id,)))