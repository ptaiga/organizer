from django.urls import path

from . import views

app_name = 'organizer'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/<int:pk>/', views.ProjectView.as_view(), name='project'),
    path('tasks/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('projects/<int:project_id>/choice/', views.choice, name='choice'),
    path('projects/add/', views.projects_add, name='projects_add'),
]
