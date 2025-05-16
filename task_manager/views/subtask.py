from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from task_manager.models.subtask import SubTask
from task_manager.serializers.subtask import SubTaskSerializer


class SubTaskListCreateView(ListCreateAPIView):
    page_size = 5
    serializer_class = SubTaskSerializer
    queryset = SubTask.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubTaskSerializer
    queryset = SubTask.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

