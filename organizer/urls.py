from django.urls import path

from . import views

app_name = 'organizer'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('projects/<int:pk>/', views.ProjectView.as_view(), name='project'),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('tasks/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('projects/add/', views.projects_add, name='projects_add'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('projects/<int:project_id>/del/', views.projects_del, name='projects_del'),    
    path('projects/<int:project_id>/tasks_del/', views.tasks_del, name='tasks_del'),
    path('about/', views.about, name='about'),
]
