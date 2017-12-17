from django.urls import path

from . import views

app_name = 'organizer'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('projects/<int:project_id>/choice/', views.choice, name='choice'),
]