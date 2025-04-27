from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "task_manager"


urlpatterns = [
    path('tasks/create/', views.create_task),
    path('tasks/', views.read_tasks),
    path('tasks/<int:pk>/', views.task_detail),
    path('tasks_by_category/', views.category_task_quantity),
    path('tasks_count/', views.task_quantity),
    path('tasks_expired/', views.task_expired),

]

