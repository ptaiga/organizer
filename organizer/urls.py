from django.urls import path

from . import views

app_name = 'organizer'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/0/', views.show, {'show_type': 'inbox'}),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('show/<str:show_type>/', views.show, name='show'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('projects/add/', views.projects_add, name='projects_add'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/<int:task_id>/comments/save', views.comments_save, name='comments_save'),
    path('projects/<int:project_id>/del/', views.projects_del, name='projects_del'),    
    path('projects/<int:project_id>/tasks_apply/', views.tasks_del, name='tasks_apply'),
    path('tasks/<int:task_id>/comments_hide/', views.comments_hide, name='comments_hide'),
    path('about/', views.about, name='about'),
    path('projects/<int:project_id>/rename/', views.projects_rename, name='projects_rename'),
    path('tasks/<int:task_id>/change/', views.tasks_change, name='tasks_change'),
    path('projects/deleted_projects/', views.deleted_projects, name='deleted_projects'),
    path('projects/<int:project_id>/deleted_tasks/', views.deleted_tasks, name='deleted_tasks'),
]
