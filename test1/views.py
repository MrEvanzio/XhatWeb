from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject


def index(request):
    title = "Django Course!!"
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    return render(request, 'about.html')


def hello(request, username):
    print(username)
    return render(request, 'projects')


def projects(request):
    projects = list(Project.objects.all())
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def create_project(request):
    return render(request, 'projects/create_project.html')


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        # show the page
        return render(request, 'task/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):

    if request.method == 'GET':
        # show the page
        return render(request, 'projects/create_project.html', {
            'forms': CreateNewProject()
        })
    else:
        print(request.POST)
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request,id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'projects/detail.html',{
        'project':project
    })