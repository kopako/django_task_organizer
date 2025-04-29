from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from task_manager.models.category import Category
from task_manager.serializers.category import CategorySerializer


@api_view(['GET'])
def category_task_quantity(request):
    task_quantity = Category.objects.annotate(task_count=Count("task"))
    serializer = CategorySerializer(data=task_quantity, many=True)
    serializer.is_valid()
    return Response(serializer.data)