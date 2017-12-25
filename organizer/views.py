from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Project, Task

class IndexView(generic.ListView):
    template_name = 'organizer/index.html'
    context_object_name = 'project_list'
    def get_queryset(self):
        return Project.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class ProjectView(generic.DetailView):
    model = Project
    template_name = 'organizer/project.html'
    def get_queryset(self):
        """
        Excludes any projects that aren't published yet.
        """
        return Project.objects.filter(pub_date__lte=timezone.now())

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

def projects_add(request):
    project_name = request.POST['project_name']
    p = Project(project_name=project_name, pub_date=timezone.now())
    p.save()
    return HttpResponseRedirect(reverse('organizer:index', args=()))

def tasks_add(request):
    project_id = request.POST['project_id']
    task_name = request.POST['task_name']
    project = get_object_or_404(Project, pk=project_id)
    t = Task(project=project, task_name=task_name, pub_date=timezone.now())
    t.save()
    return HttpResponseRedirect(reverse('organizer:project', args=(project_id,)))
