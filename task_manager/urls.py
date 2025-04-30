from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.category import CategoryViewSet
from .views.subtask import SubTaskListCreateView, SubTaskDetailUpdateDeleteView
from .views.task import task_quantity, task_expired, TaskRetrieveUpdateDestroyAPIView, TaskListCreateAPIView

app_name = "task_manager"

router = DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('tasks_count/', task_quantity),
    path('tasks_expired/', task_expired),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('', include(router.urls)),
]
