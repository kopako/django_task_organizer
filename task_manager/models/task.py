from django.db import models

from task_manager.models.category import Category


class Task(models.Model):
    STATUS_CHOICES = {
        'New': 'New',
        'In progress': 'In progress',
        'Pending': 'Pending',
        'Blocked': 'Blocked',
        'Done': 'Done',
    }
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "task_manager_task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ("-created_at",)
        unique_together = ("title",)
        default_related_name = "task"

