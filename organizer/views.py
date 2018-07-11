from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail

from dateutil.relativedelta import relativedelta

import markdown, json

from .models import Project, Task, Comment
from .functions import get_project_list, get_task_list, get_task_count

from sorga.private_settings import email_to, email_from, \
                                    email_auth_user, email_auth_password

def index(request):
    return HttpResponseRedirect(reverse('organizer:show', args=('inbox',)))

def show(request, show_type, project_id=None):
    user = request.user if request.user.is_authenticated else None
    sort = '-pub_date'

    done_flag = True if 'done_tasks' in request.GET else False
    if 'sort' in request.GET:
       if request.GET['sort'] == 'latest': sort='pub_date'
    elif 'sort' in request.COOKIES:
        if request.COOKIES['sort'] == 'latest': sort='pub_date'

    project = None
    if show_type == 'hidden':
        project_list = get_project_list(user, True)
    elif show_type == 'project':
        project = get_object_or_404(Project, pk=project_id, user=user)
        project_list = get_project_list(user, project.done_flag)
        show_type = ''
    else:
        project_list = get_project_list(user)
    task_list = get_task_list(user, project, done_flag, show_type) \
                    .exclude(snooze_date__date=timezone.now()
                                .date()).order_by('priority', sort)

    num_inbox_tasks, num_today_tasks, num_week_tasks = \
        get_task_count(user)

    response = render(request, 'organizer/index.html', {
        'project_list': project_list,
        'project': project,
        'task_list': task_list,
        'num_inbox_tasks': num_inbox_tasks,
        'num_today_tasks': num_today_tasks,
        'num_week_tasks': num_week_tasks,
        'active': show_type
    })
    if 'sort' in request.GET: response.set_cookie('sort', request.GET['sort'])
    return response

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
            if task.repeat:
                task.due_date += \
                    relativedelta(days=1) if task.repeat == "daily" \
                    else relativedelta(weeks=1) if task.repeat == "weekly" \
                    else relativedelta(months=1)
            else:
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
    repeat = request.POST['task_repeat'] \
        if request.POST['task_repeat'] != "none" else None
    snooze = request.POST['task_snooze'] \
        if request.POST['task_snooze'] != "none" else None
    priority = request.POST['priority']
    due_date_d = request.POST['due_date_d']
    due_date_t = request.POST['due_date_t']
    task = get_object_or_404(Task, pk=task_id, user=user)
    project = get_object_or_404(Project, pk=project_id, user=user) \
        if project_id else None
    project_id = task.project.id if task.project else 0
    task.project = project
    task.task_name = task_name
    task.done_flag = done_flag
    task.repeat = repeat
    task.snooze_date = timezone.now() if snooze == "today" else None
    task.priority = priority
    task.due_date = (due_date_d + 'T' \
                            + (due_date_t if due_date_t else '00:00') \
                            + '+00') if due_date_d else None
    task.save()
    return HttpResponseRedirect(reverse('organizer:project', \
        args=(project_id,)))

def about(request):
    # user = request.user if request.user.is_authenticated else None
    # return HttpResponse(f"Hi, {user}! Sorga - simple organizer app. Version 0.3.0")
    with open('README.md') as f:
        content = f.read()
    content = markdown.markdown(content, ['markdown.extensions.nl2br'])
    return HttpResponse(content)

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

def export(request, mode):
    user = request.user if request.user.is_authenticated else None
    projects = Project.objects.filter(user=user)
    data = {}
    data['user'] = user
    data['inbox'] = []
    inbox_tasks = Task.objects.filter(user=user, project=None)
    for t in inbox_tasks:
        data['inbox'].append({
            'task_name': t.task_name,
            'pub_date': t.pub_date.isoformat() if t.pub_date else t.pub_date,
            'done_flag': t.done_flag,
            'due_date': t.due_date.isoformat() if t.due_date else t.due_date,
            'repeat': t.repeat,
            'snooze_date': t.snooze_date.isoformat() if t.snooze_date else t.snooze_date,
            'priority': t.priority
        })
    data['projects'] = []
    for p in projects:
        tasks = []
        for t in p.task_set.all():
            tasks.append({
                'task_name': t.task_name,
                'pub_data': t.pub_date.isoformat(),
                'done_flag': t.done_flag,
                'due_date': t.due_date.isoformat() if t.due_date else t.due_date,
                'repeat': t.repeat,
                'snooze_date': t.snooze_date.isoformat() if t.snooze_date else t.snooze_date,
                'priority': t.priority
            })
        data['projects'].append({
            'project_name': p.project_name,
            'pub_date': p.pub_date.isoformat(),
            'done_flag': p.done_flag,
            'tasks': tasks
        })

    if mode == 'json':
        response = HttpResponse(json.dumps(data), content_type="application/vnd.json")
        response['Content-Disposition'] = 'attachment;filename="export.json"'
        return response

    if mode == 'txt':
        def parse_json_to_txt(data, count=0):
            response = ''
            for key in data:
                if type(data[key]) == list:
                    response += '\t'*count + key + ':\n'
                    for elem in data[key]:
                        if type(elem) == dict:
                            response += parse_json_to_txt(elem, count+1) + '\n'
                        else:
                            response += '\t'*count + str(elem) + '\n'
                else:
                    response += '\t'*count + key + ': ' + str(data[key]) + '\n'
                # response += '\n'
            return response
        return HttpResponse(parse_json_to_txt(data), content_type="text/plain")

    if mode == 'html':
        def parse_json_to_html(data, count=2):
            response = ''
            for key in data:
                if type(data[key]) == list:
                    response += f'<h{count}><u>{key}</u></h{count}>'
                    for elem in data[key]:
                        if type(elem) == dict:
                            response += parse_json_to_html(elem, count+1) + '<br>'
                        else:
                            response += f'<h{count}>{elem}</h{count}>'
                else:
                    response += f'<b>{key}</b>: {data[key]}<br>'
            return response
        return HttpResponse(parse_json_to_html(data))

    return HttpResponse(json.dumps(data), content_type="text/plain")
