from django.urls import path

from . import views

app_name = 'organizer'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<str:show_type>/', views.show, name='show'),
    path('projects/0/', views.show, {'show_type': 'inbox'}),
    path('projects/<int:project_id>/', views.show, {'show_type': 'project'}, name='project'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('projects/add/', views.projects_add, name='projects_add'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/<int:task_id>/comments/save', views.comments_save, name='comments_save'),
    path('projects/<int:project_id>/<str:status>/', views.projects_change, name='projects_change'),
    path('projects/<int:project_id>/tasks_apply/', views.tasks_del, name='tasks_apply'),
    path('tasks/<int:task_id>/comments_hide/', views.comments_hide, name='comments_hide'),
    path('projects/<int:project_id>/rename/', views.projects_rename, name='projects_rename'),
    path('tasks/<int:task_id>/change/', views.tasks_change, name='tasks_change'),
    path('about/', views.about, name='about'),
    path('send/', views.send, name='send'),
]
