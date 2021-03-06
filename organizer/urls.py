from django.urls import path

from . import views

app_name = 'organizer'
urlpatterns = [
    path('', views.show, {'show_type': 'today'}, name='index'),
    path('project/<int:project_id>/', views.show, name='project'),
    path('sort/<str:show_type>/<int:project_id>/', views.show, name='sort'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('projects/add/', views.projects_add, name='projects_add'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/<int:task_id>/comments/save', views.comments_save, name='comments_save'),
    path('projects/<str:project_id>/tasks_apply/', views.tasks_apply, name='tasks_apply'),
    path('projects/<int:project_id>/<str:status>/', views.projects_change, name='projects_change'),
    path('tasks/<int:task_id>/comments_hide/', views.comments_hide, name='comments_hide'),
    path('tasks/<int:task_id>/change/', views.tasks_change, name='tasks_change'),
    path('about/', views.about, name='about'),
    path('send/', views.send, name='send'),
    path('export/', views.export, {'mode': 'other'}, name='export'),
    path('export/<str:mode>/', views.export, name='export'),
    path('<slug:show_type>/', views.show, name='show'),
]
