from django.urls import path

from . import views

app_name='account'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_changes', views.save_changes, name='save_changes'),
    path('send_daily_mail', views.send_daily_mail, name='send_daily_mail'),
    path('random_task', views.random_task, name='random_task'),
]
