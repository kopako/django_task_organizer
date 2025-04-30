from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

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

class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubTaskSerializer
    queryset = SubTask.objects.all()

