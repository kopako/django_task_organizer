from django.urls import path

from .views.category import category_task_quantity
from .views.subtask import SubTaskListCreateView, SubTaskDetailUpdateDeleteView
from .views.task import create_task, read_tasks, task_detail, task_quantity, task_expired

app_name = "task_manager"


urlpatterns = [
    path('tasks/create/', create_task),
    path('tasks/', read_tasks),
    path('tasks/<int:pk>/', task_detail),
    path('tasks_by_category/', category_task_quantity),
    path('tasks_count/', task_quantity),
    path('tasks_expired/', task_expired),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
]

