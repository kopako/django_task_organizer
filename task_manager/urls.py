from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views.category import CategoryViewSet
from .views.subtask import SubTaskListCreateView, SubTaskDetailUpdateDeleteView
from .views.task import task_quantity, task_expired, TaskRetrieveUpdateDestroyAPIView, TaskListCreateAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "task_manager"

schema_view = get_schema_view(
 openapi.Info(
 title="Task Manager",
 default_version='v1',
 description="",
 terms_of_service="https://www.google.com/policies/terms/",
 contact=openapi.Contact(email="contact@local.com"),
 license=openapi.License(name="BSD License"),
 ),
 public=True,
 permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth-login-jwt/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),
    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view()),
    path('tasks_count/', task_quantity),
    path('tasks_expired/', task_expired),
    path('subtasks/', SubTaskListCreateView.as_view()),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view()),
] + router.urls
