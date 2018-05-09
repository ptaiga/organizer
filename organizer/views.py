from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail

from .models import Project, Task, Comment
from .functions import get_project_list, get_task_list, get_task_count

from sorga.private_settings import email_to, email_from, \
                                    email_auth_user, email_auth_password

def index(request):
    return HttpResponseRedirect(reverse('organizer:show', args=('inbox',)))

def show(request, show_type, project_id=None):
    user = request.user if request.user.is_authenticated else None
    sort = '-pub_date'
    if 'sort' in request.GET:
       if request.GET['sort'] == 'latest': sort='pub_date'
    done_flag = True if 'done_tasks' in request.GET else False

    project = None
    if show_type == 'hidden':
        project_list = get_project_list(user, True)
    elif show_type == 'project':
        project = get_object_or_404(Project, pk=project_id, user=user)
        project_list = get_project_list(user, project.done_flag)
        show_type = ''
    else:
        project_list = get_project_list(user)
    task_list = get_task_list(user, project, done_flag, show_type).order_by(sort)

    num_inbox_tasks, num_today_tasks, num_week_tasks = \
        get_task_count(user)

    return render(request, 'organizer/index.html', {
        'project_list': project_list,
        'project': project,
        'task_list': task_list,
        'num_inbox_tasks': num_inbox_tasks,
        'num_today_tasks': num_today_tasks,
        'num_week_tasks': num_week_tasks,
        'active': show_type
    })

def task(request, task_id):
    user = request.user if request.user.is_authenticated else None
    task = get_object_or_404(Task, pk=task_id, user=user)
    if 'refer' in request.GET:
        refer = request.GET['refer']
    else:
        refer = ''
    if refer == 'hidden':
        flag = True
    elif not task.project:
        flag = False
    else:
        flag = task.project.done_flag
    project_list = get_project_list(user, flag)
    comment_list = Comment.objects.filter(task=task, status_flag=True)
    num_inbox_tasks, num_today_tasks, num_week_tasks = \
        get_task_count(user)
    comment = None
    if 'comment_edit' in request.GET:
        comment_id = request.GET['comment_edit']
        comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'organizer/task.html', {
        'project_list': project_list,
        'project': task.project,
        'task': task,
        'comment_list': comment_list,
        'num_inbox_tasks': num_inbox_tasks,
        'num_today_tasks': num_today_tasks,
        'num_week_tasks': num_week_tasks,
        'comment': comment,
        'active': refer,
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

def comments_save(request, task_id):
    user = request.user if request.user.is_authenticated else None
    comment_text = request.POST['comment_text']
    task = get_object_or_404(Task, pk=task_id, user=user)
    if 'comment_id' in request.POST:
        comment_id = request.POST['comment_id']
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.comment_text = comment_text
        comment.last_edit_date = timezone.now()
        comment.save()
    else:
        Comment(user=user, task=task, comment_text=comment_text).save()
    return HttpResponseRedirect(reverse('organizer:task', args=(task_id,)))

def projects_change(request, project_id, status):
    user = request.user if request.user.is_authenticated else None
    project = get_object_or_404(Project, pk=project_id, user=user)
    if status == 'activate':
        project.done_flag = False
    else:
        project.done_flag = True
    project.save()
    return HttpResponseRedirect(reverse('organizer:index'))

def tasks_del(request, project_id):
    user = request.user if request.user.is_authenticated else None
    project = get_object_or_404(Project, pk=project_id, user=user) \
        if project_id else None

    for key in request.POST:
        if key.startswith('task'):
            task = get_object_or_404(Task, pk=request.POST[key],
                project = project, user=user)
            task.done_flag = True
            task.save()

    return HttpResponseRedirect(reverse('organizer:project', \
        args=(project_id,)))

def comments_hide(request, task_id):
    user = request.user if request.user.is_authenticated else None
    get_object_or_404(Task, pk=task_id, user=user) # verify task and user
    comment_id = request.POST['comment_id']
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.status_flag = False
    comment.save()
    return HttpResponseRedirect(reverse('organizer:task', args=(task_id,)))

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
    done_flag = (request.POST['done_flag'] == "True")
    due_date_d = request.POST['due_date_d']
    due_date_t = request.POST['due_date_t']
    task = get_object_or_404(Task, pk=task_id, user=user)
    project = get_object_or_404(Project, pk=project_id, user=user) \
        if project_id else None
    project_id = task.project.id if task.project else 0
    task.project = project
    task.task_name = task_name
    task.done_flag = done_flag
    task.due_date = (due_date_d + 'T' \
                            + (due_date_t if due_date_t else '00:00') \
                            + '+00') if due_date_d else None
    task.save()
    return HttpResponseRedirect(reverse('organizer:project', \
        args=(project_id,)))

def about(request):
    user = request.user if request.user.is_authenticated else None
    return HttpResponse(f"Hi, {user}! Sorga - simple organizer app. Version 0.3.0")

def intro(request):
    return render(request, 'organizer/intro.html')

def send(request):
    email = request.POST['email']
    if send_mail(
        '[Organizer] A new user is registered',
        email,
        email_from,
        [email_to],
        fail_silently=False,
        auth_user=email_auth_user,
        auth_password=email_auth_password
    ):
        return HttpResponse("Your request has been successfully sent. \
            Please wait for an answer.")
    else:
        return HttpResponse("Your request doesn't send. Try again later")
