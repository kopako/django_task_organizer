from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader


from task_manager.models import Task

# Create your views here.
def index(request):
    template = loader.get_template("task_manager/index.html")
    tasks = Task.objects.order_by("id")
    context = {
        "tasks": tasks,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, "task_manager/detail.html", {"task": task})
