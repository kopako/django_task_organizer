from django.db import models
from django.utils import timezone

from task_manager.managers import SoftDeleteManager


class Category(models.Model):
    objects = SoftDeleteManager()
    name = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)
        unique_together = ("name",)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
