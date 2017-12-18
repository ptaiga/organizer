from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Project, Task

class IndexView(generic.ListView):
    template_name = 'organizer/index.html'
    context_object_name = 'project_list'
    def get_queryset(self):
        return Project.objects.all()

class ProjectView(generic.DetailView):
    model = Project
    template_name = 'organizer/project.html'

class TaskView(generic.DetailView):
    model = Task
    template_name = 'organizer/task.html'

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