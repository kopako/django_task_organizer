from rest_framework import status, generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from task_manager.models.subtask import SubTask
from task_manager.serializers.subtask import SubTaskSerializer


class SubTaskListCreateView(APIView, PageNumberPagination):
    page_size = 5

    def get(self, request):
        sort_by = request.query_params.get('sort_by', 'created_at')
        sort_order = request.query_params.get('sort_order', 'desc')
        title = request.query_params.get('title')
        status = request.query_params.get('status')
        if sort_order == 'desc':
            sort_by = f'-{sort_by}'
        page_size = self.get_page_size(request)
        self.page_size = page_size or self.page_size
        subtasks = SubTask.objects.order_by(sort_by)
        if title:
            subtasks = SubTask.objects.filter(title__iexact=title)
        if status:
            subtasks = SubTask.objects.filter(status__iexact=status)
        results = self.paginate_queryset(subtasks, request, view=self)
        serializer = SubTaskSerializer(results, many=True)
        return  self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = SubTaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        try:
            subtask = SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return Response({'error': 'SubTask not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            subtask = SubTask.objects.get(pk=pk)

        except SubTask.DoesNotExist:
            return Response({'error': 'SubTask not found'},
                    status=status.HTTP_404_NOT_FOUND)
        serializer = SubTaskSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            subtask = SubTask.objects.get(pk=pk)
        except SubTask.DoesNotExist:
            return Response({'error': 'SubTask not found'},
                            status=status.HTTP_404_NOT_FOUND)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
