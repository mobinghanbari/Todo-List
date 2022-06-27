from django.urls import path
from .views import TaskList, TaskDetail, CreateView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', CreateView.as_view(), name='task-create'),
]