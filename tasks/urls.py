from django.urls import path
from .views import TaskApiView

app_name = 'tasks'

urlpatterns = [
    path('list-task/', TaskApiView.as_view(), name='list_task')
]
