from django import contrib
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from task_manager.models.subtask import SubTask
from task_manager.permissions import IsOwnerOrReadOnly
from task_manager.serializers.subtask import SubTaskSerializer


class SubTaskListCreateView(ListCreateAPIView):
    page_size = 5
    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, contrib.auth.models.AnonymousUser):
            return SubTask.objects.none()
        else:
            return SubTask.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubTaskSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, contrib.auth.models.AnonymousUser):
            return SubTask.objects.none()
        else:
            return SubTask.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

