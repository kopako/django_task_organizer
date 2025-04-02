from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name}"

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

