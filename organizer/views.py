from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Project, Task, Comment
from .functions import get_project_list, get_task_list

def index(request):
    user = request.user if request.user.is_authenticated else None
    project_list = get_project_list(user)
    task_list = get_task_list(user, None)
    return render(request, 'organizer/index.html', {
        'project_list': project_list,
        'task_list': task_list,
    })

def project(request, project_id):
    user = request.user if request.user.is_authenticated else None
    project = get_object_or_404(Project, pk=project_id, user=user)
    project_list = get_project_list(user, project.done_flag)
    task_list = get_task_list(user, project, project.done_flag)
    return render(request, 'organizer/index.html', {
        'project_list': project_list,
        'project': project,
        'task_list': task_list,
    })

def task(request, task_id):
    user = request.user if request.user.is_authenticated else None
    task = get_object_or_404(Task, pk=task_id, user=user)
    flag = False if not task.project else task.project.done_flag
    project_list = get_project_list(user, flag)
    comment_list = Comment.objects.filter(task=task)
    return render(request, 'organizer/task.html', {
        'project_list': project_list,
        'task': task,
        'comment_list': comment_list,
    })

def projects_add(request):
    user = request.user if request.user.is_authenticated else None
    project_name = request.POST['project_name']
    p = Project(
        user=user,
        project_name=project_name,
        pub_date=timezone.now()
    )
    p.save()
    return HttpResponseRedirect(reverse('organizer:index', args=()))

def tasks_add(request):
    user = request.user if request.user.is_authenticated else None
    project_id = request.POST['project_id'] or 0
    task_name = request.POST['task_name']
    project = \
        get_object_or_404(Project, pk=project_id, user=user) \
            if project_id else None
    Task(project=project, task_name=task_name, user=user).save()
    return HttpResponseRedirect(reverse('organizer:project',
        args=(project_id,)))

def comments_add(request, task_id):
    user = request.user if request.user.is_authenticated else None
    comment_text = request.POST['comment_text']
    task = get_object_or_404(Task, pk=task_id, user=user)
    Comment(task=task, comment_text=comment_text).save()
    return HttpResponseRedirect(reverse('organizer:task', args=(task_id,)))

def projects_del(request, project_id):
    user = request.user if request.user.is_authenticated else None
    project = get_object_or_404(Project, pk=project_id, user=user)
    project.done_flag = True
    project.save()
    return HttpResponseRedirect(reverse('organizer:index'))

def tasks_del(request, project_id):
    user = request.user if request.user.is_authenticated else None
    project = get_object_or_404(Project, pk=project_id, user=user) \
        if project_id else None
    try:
        selected_task = Task.objects.get(project=project, pk=request.POST['task'])
    except (KeyError, Task.DoesNotExist):
        project_list = get_project_list(user, project.done_flag)
        task_list = get_task_list(user, project)
        return render(request, 'organizer/project.html', {
            'project_list': project_list,
            'task_list': task_list,
            'project': project,
            'error_message': "You didn't select a task."
        })
    else:
        selected_task.done_flag = True
        selected_task.save()
        return HttpResponseRedirect(reverse('organizer:project', \
            args=(project_id,)))

def comments_del(request, task_id):
    user = request.user if request.user.is_authenticated else None
    get_object_or_404(Task, pk=task_id, user=user) # verify task and user
    comment_id = request.POST['comment_id']
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('organizer:task', args=(task_id,)))

def about(request):
    user = request.user if request.user.is_authenticated else None
    return HttpResponse(f"Hi, {user}! Sorga - simple organizer app. Version 0.2.0")

def projects_rename(request, project_id):
    user = request.user if request.user.is_authenticated else None
    p = get_object_or_404(Project, pk=project_id, user=user)
    project_name = request.POST['project_name']
    p.project_name = project_name
    p.save()
    return HttpResponseRedirect(reverse('organizer:project', args=(project_id,)))

def tasks_change(request, task_id):
    user = request.user if request.user.is_authenticated else None
    task_name = request.POST['task_name']
    project_id = int(request.POST['project_select'])
    due_date_d = request.POST['due_date_d']
    due_date_t = request.POST['due_date_t']
    task = get_object_or_404(Task, pk=task_id, user=user)
    project = get_object_or_404(Project, pk=project_id, user=user) \
        if project_id else None
    project_id = task.project.id if task.project else 0
    task.project = project
    task.task_name = task_name
    task.due_date = (due_date_d + (' '+due_date_t if due_date_t else '')) \
        if due_date_d else None
    task.save()
    return HttpResponseRedirect(reverse('organizer:project', \
        args=(project_id,)))

def deleted_projects(request):
    user = request.user if request.user.is_authenticated else None
    project_list = get_project_list(user, True)
    task_list = get_task_list(user, None, False)
    return render(request, 'organizer/index.html', {
        'project_list': project_list,
        'task_list': task_list
    })

def deleted_tasks(request, project_id):
    user = request.user if request.user.is_authenticated else None
    project = get_object_or_404(Project, pk=project_id, user=user) \
        if project_id else None
    task_list = get_task_list(user, project, True)
    flag = False if not project else project.done_flag
    project_list = get_project_list(user, flag)
    return render(request, 'organizer/index.html', {
        'project_list': project_list,
        'task_list': task_list,
        'project': project
    })
