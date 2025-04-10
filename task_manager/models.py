from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table =  'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)
        unique_together = ("name",)


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=250,unique_for_year="created_at")
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.title}"
    class Meta:
        db_table = "task_manager_task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ("-created_at",)
        unique_together = ("title",)

class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=250,unique_for_year="created_at")
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    main_task = models.ForeignKey( # Main task, M2O
        Task,
        on_delete=models.CASCADE,
        null=False,
    )
    def __str__(self):
        return self.title
    class Meta:
        db_table = "task_manager_subtask"
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
        ordering = ("-created_at",)
        unique_together = ("title",)

