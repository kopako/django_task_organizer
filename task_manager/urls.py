from django.urls import path

from .views.category import category_task_quantity
from .views.subtask import SubTaskListCreateView, SubTaskDetailUpdateDeleteView
from .views.task import task_quantity, task_expired, TaskRetrieveUpdateDestroyAPIView, TaskListCreateAPIView

app_name = "task_manager"


urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('tasks_by_category/', category_task_quantity),
    path('tasks_count/', task_quantity),
    path('tasks_expired/', task_expired),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
]

