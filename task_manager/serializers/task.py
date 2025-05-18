from django.utils import timezone
from rest_framework import serializers

from task_manager.models.task import Task
from task_manager.serializers.category import CategorySerializer
from task_manager.serializers.subtask import SubTaskSerializer


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
        read_only_fields = ['owner','created_at']

class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer()
    class Meta:
        model = Task
        fields = '__all__'

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task

    def validate_deadline(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Deadline can't be earlier then creation.")
        return value
