from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "task_manager"

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'subtasks', views.SubTaskViewSet)
router.register(r'categories', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('tasks_by_category/', views.category_task_quantity),
    path('tasks_count/', views.task_quantity),
    path('tasks_expired/', views.task_expired),
    
]
