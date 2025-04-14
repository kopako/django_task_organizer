from django.contrib import admin

from task_manager.models import (Task, SubTask, Category)

class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 3


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'deadline', 'created_at')
    list_per_page = 10
    inlines = [SubTaskInline]
    
    def short_title(self, obj):
        if len(obj.title) < 10:
            return obj.title
        return f"{obj.title[:10]}..."
    
    def change_status(self, request, objects):
        for obj in objects:
            obj.status = Task.STATUS_CHOICES['Done']
            obj.save()
        return objects

    change_status.short_description = 'Mark as Done'
    
    actions = ['change_status']

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'deadline', 'created_at')
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)