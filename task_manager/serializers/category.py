from rest_framework import serializers

from task_manager.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    task_count = serializers.IntegerField(required=False)
    class Meta:
        model = Category
        fields = ['name', 'task_count']

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        if Category.objects.filter(name__iexact=validated_data.get('name')).exists():
            raise serializers.ValidationError(f'Category exists: {validated_data.get('name')}')
        super().create(validated_data)

    def update(self, instance, validated_data):
        if Category.objects.filter(name__iexact=validated_data.get('name')).exists():
            raise serializers.ValidationError(f'Category exists: {validated_data.get('name')}')
        super().update(instance, validated_data)