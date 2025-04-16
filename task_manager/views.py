from django.utils import timezone

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum, Count


from task_manager.models import *
from task_manager.serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

@api_view(['GET'])
def category_task_quantity(request):
    task_quantity = Category.objects.annotate(task_count=Count("task"))
    serializer = CategorySerializer(data=task_quantity, many=True)
    serializer.is_valid()
    return Response(serializer.data)

@api_view(['GET'])
def task_quantity(request):
    task_count: int = Task.objects.all().count()
    return Response(data={'task_count':task_count})

@api_view(['GET'])
def task_expired(request):
    task_expired = Task.objects.filter(deadline__lt=timezone.now())
    ser = TaskSerializer(data=task_expired, many=True)
    ser.is_valid()
    return Response(data=ser.data)
