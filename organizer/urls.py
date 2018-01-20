from django.urls import path

from . import views

app_name = 'organizer'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('projects/<int:pk>/', views.ProjectView.as_view(), name='project'),
    # path('tasks/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('', views.index, name='index'),
    path('projects/0/', views.index),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('projects/add/', views.projects_add, name='projects_add'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/<int:task_id>/comments/add', views.comments_add, name='comments_add'),
    path('projects/<int:project_id>/del/', views.projects_del, name='projects_del'),    
    path('projects/<int:project_id>/tasks_del/', views.tasks_del, name='tasks_del'),
    path('tasks/<int:task_id>/comments_del/', views.comments_del, name='comments_del'),
    path('about/', views.about, name='about'),
    path('projects/<int:project_id>/rename/', views.projects_rename, name='projects_rename'),
    path('tasks/<int:task_id>/change/', views.tasks_change, name='tasks_change'),
    path('projects/deleted_projects/', views.deleted_projects, name='deleted_projects'),
    path('projects/<int:project_id>/deleted_tasks/', views.deleted_tasks, name='deleted_tasks'),
]
