from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Project, Task, Comment

# class IndexView(generic.ListView):
#     template_name = 'organizer/index.html'
#     context_object_name = 'project_list'
#     def get_queryset(self):
#         return Project.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

# class ProjectView(generic.DetailView):
#     model = Project
#     template_name = 'organizer/project.html'
#     def get_queryset(self):
#         """
#         Excludes any projects that aren't published yet.
#         """
#         return Project.objects.filter(pub_date__lte=timezone.now())

# class TaskView(generic.DetailView):
#     model = Task
#     template_name = 'organizer/task.html'

def index(request):
    project_list = \
        Project.objects.filter(pub_date__lte=timezone.now(), done_flag=False)\
            .order_by('-pub_date')
    task_list = Task.objects.filter(project=None, done_flag=False)
    return render(request, 'organizer/index.html', {
        'project_list': project_list,
        'task_list': task_list,
    })

def project(request, project_id):
    project_list = \
        Project.objects.filter(pub_date__lte=timezone.now(), done_flag=False)\
            .order_by('-pub_date')
    project = get_object_or_404(Project, pk=project_id)
    task_list = Task.objects.filter(project=project, done_flag=False)
    return render(request, 'organizer/project.html', {
        'project_list': project_list,
        'project': project,
        'task_list': task_list,
    })

def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    comment_list = Comment.objects.filter(task=task)
    return render(request, 'organizer/task.html', {
        'task': task,
        'comment_list': comment_list,
    })

def projects_add(request):
    project_name = request.POST['project_name']
    p = Project(project_name=project_name, pub_date=timezone.now())
    p.save()
    return HttpResponseRedirect(reverse('organizer:index', args=()))

def tasks_add(request):
    project_id = request.POST['project_id']
    task_name = request.POST['task_name']
    if project_id:
        project = get_object_or_404(Project, pk=project_id)
        t = Task(project=project, task_name=task_name)
        t.save()
        return HttpResponseRedirect(reverse('organizer:project', args=(project_id,)))
    else:
        t = Task(task_name=task_name)
        t.save()
        return HttpResponseRedirect(reverse('organizer:index', args=()))

def comments_add(request, task_id):
    comment_text = request.POST['comment_text']
    task = get_object_or_404(Task, pk=task_id)
    c = Comment(task=task, comment_text=comment_text)
    c.save()
    return HttpResponseRedirect(reverse('organizer:task', args=(task_id,)))

def projects_del(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    # project.delete()
    project.done_flag = True
    project.save()
    return HttpResponseRedirect(reverse('organizer:index'))

def tasks_del(request, project_id):
    if project_id:
        project = get_object_or_404(Project, pk=project_id)
        try:
            selected_task = project.task_set.get(pk=request.POST['task'])
        except (KeyError, Task.DoesNotExist):
            project_list = \
                Project.objects.filter(pub_date__lte=timezone.now(), done_flag=False)\
                    .order_by('-pub_date')
            return render(request, 'organizer/project.html', {
                'project_list': project_list,
                'project': project,
                'error_message': "You didn't select a task."
            })
        else:
            # selected_task.delete()
            selected_task.done_flag = True
            selected_task.save()
            return HttpResponseRedirect(reverse('organizer:project', \
                args=(project_id,)))
    else:
        try:
            selected_task = Task.objects.get(pk=request.POST['task'])
        except (KeyError, Task.DoesNotExist):
            project_list = \
                Project.objects.filter(pub_date__lte=timezone.now(), done_flag=False)\
                    .order_by('-pub_date')
            task_list = Task.objects.filter(project=None, done_flag=False)
            return render(request, 'organizer/index.html', {
                'project_list': project_list,
                'task_list': task_list,
                'error_message': "You didn't select a task."
            })
        else:
            # selected_task.delete()
            selected_task.done_flag = True
            selected_task.save()
            return HttpResponseRedirect(reverse('organizer:index', \
                args=()))

def comments_del(request, task_id):
    comment_id = request.POST['comment_id']
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('organizer:task', args=(task_id,)))

def about(request):
    return HttpResponse("Sorga - simple organizer app. Version 0.1.0")

def projects_rename(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    project_name = request.POST['project_name']
    p.project_name = project_name
    p.save()
    return HttpResponseRedirect(reverse('organizer:project', args=(project_id,)))

def tasks_change(request, task_id):
    task_name = request.POST['task_name']
    due_date_d = request.POST['due_date_d']
    due_date_t = request.POST['due_date_t']
    task = get_object_or_404(Task, pk=task_id)
    task.task_name = task_name
    if due_date_d:
        if due_date_t:
            task.due_date = f'{due_date_d} {due_date_t}'
        else:
            task.due_date = due_date_d
    else:
        task.due_date = None
    task.save()
    return HttpResponseRedirect(reverse('organizer:project', \
        args=(task.project.id,)))

def deleted_projects(request):
    project_list = \
        Project.objects.filter(done_flag=True).order_by('-pub_date')
    return render(request, 'organizer/deleted.html', {
        'project_list': project_list,
    })

def deleted_tasks(request, project_id):
    if project_id:
        project = get_object_or_404(Project, pk=project_id)
    else:
        project = None
    task_list = Task.objects.filter(project=project, done_flag=True)
    return render(request, 'organizer/deleted.html', {
        'task_list': task_list,
    })
