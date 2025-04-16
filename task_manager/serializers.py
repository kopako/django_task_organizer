from task_manager.models import *
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    task_count = serializers.IntegerField(required=False)
    class Meta:
        model = Category
        fields = ['name', 'task_count']

class TaskSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'categories',
            'status',
            'deadline',
            'created_at'
        ]


class SubTaskSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = SubTask
        fields = [
            'title',
            'description',
            'categories',
            'status',
            'deadline',
            'created_at'
        ]
