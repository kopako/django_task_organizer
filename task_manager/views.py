from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum, Count


from task_manager.models import *
from task_manager.serializers import *

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def read_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Book not found'},
                status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
