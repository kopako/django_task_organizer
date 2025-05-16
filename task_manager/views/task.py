from django.utils import timezone
from rest_framework import filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from task_manager.models.task import Task
from task_manager.serializers.task import TaskSerializer


class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    permission_classes = [IsAuthenticatedOrReadOnly]

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def task_quantity(request):
    task_count: int = Task.objects.all().count()
    return Response(data={'task_count':task_count})

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def task_expired(request):
    task_expired = Task.objects.filter(deadline__lt=timezone.now())
    ser = TaskSerializer(data=task_expired, many=True)
    ser.is_valid()
    return Response(data=ser.data)
