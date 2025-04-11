from datetime import timedelta
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ichdjangoproject.settings')
django.setup()

from django.utils import timezone
from task_manager.models import *

main_task = Task(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=3)
)

sub_tasks = [
    SubTask(
        title="Gather information",
        description="Find necessary information for the presentation",
        status="New",
        deadline=timezone.now() + timedelta(days=2)
    ),
    SubTask(
        title="Create slides",
        description="Create presentation slides",
        status="New",
        deadline=timezone.now() + timedelta(days=1),
    )
]
for sub_t in sub_tasks:
    sub_t.main_task = main_task

main_task.save()
SubTask.objects.bulk_create(sub_tasks)
# ==================================================================================
[print(t) for t in Task.objects.filter(status="new")]
[print(st) for st in SubTask.objects.filter(status="done", deadline__lt=timezone.now())]
# ==================================================================================
tasks_update=Task.objects.filter(title="Prepare presentation").update(status='In progress')
st1 = SubTask.objects.get(title="Gather information")
st1.deadline = st1.deadline - timedelta(days=2)
st1.save()
st2 = SubTask.objects.get(title="Create slides")
st2.description = "Create and format presentation slides"
st2.save()
Task.objects.get(title="Prepare presentation").delete()
