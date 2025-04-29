from django.db import models

from task_manager.models.category import Category
from task_manager.models.task import Task


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),
    ]
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    main_task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        null=False,
        related_name='sub_task',
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_subtask"
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
        ordering = ("-created_at",)
        unique_together = ("title",)
