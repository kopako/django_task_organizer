from django.db.models import Count
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from task_manager.models.category import Category
from task_manager.pagination import CustomCursorPagination
from task_manager.serializers.category import CategorySerializer


class CategoryCursorPagination(CustomCursorPagination):
    ordering = 'name'


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryCursorPagination

    @action(detail=False, methods=['get'])
    def count_tasks(self, request):
        task_quantity = Category.objects.annotate(task_count=Count("task"))
        serializer = CategorySerializer(data=task_quantity, many=True)
        serializer.is_valid()
        return Response(serializer.data)
