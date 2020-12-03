from django.shortcuts import render, redirect,  get_object_or_404

from core.forms import FormTodo
from core.models import Todo


def list(request):
    todo_tasks = Todo.objects.all()
    return render(request, 'core/list.html', context={'todo_tasks': todo_tasks})


def create(request):
    if request.method == "POST":
        form = FormTodo(request.POST)
        if form.is_valid():
            object = form.save()
            return redirect('details', id=object.id)
        return render(request, 'core/form.html', context={'form': form})
    form = FormTodo()
    return render(request, 'core/form.html', context={'form': form})


def details(request, id):
    object = get_object_or_404(Todo, id=id)
    return render(request, 'core/details.html', context={"object": object})


def delete(request, id):
    object = get_object_or_404(Todo, id=id)
    object.delete()
    return redirect('list')


def update(request, id):
    object = get_object_or_404(Todo, id=id)

    if request.method == "POST":
        form = FormTodo(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('details', id=object.id)
        return render(request, 'core/form.html', context={'form': form})

    form = FormTodo(instance=object)

    return render(request, 'core/form.html', context={'form': form})
