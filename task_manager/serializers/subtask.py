from rest_framework import serializers

from task_manager.models.subtask import SubTask
from task_manager.serializers.category import CategorySerializer


class SubTaskSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ['created_at']
