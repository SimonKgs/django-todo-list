from django.shortcuts import render
from todoList.models import Todo
from todoList.forms import TodoForm


# Create your views here.
def index(request):
    context = {}
    form = TodoForm()
    todos = Todo.objects.all()
    context['todos'] = todos
    context['title'] = 'Home'

    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = TodoForm(request.POST)
            else:
                todo = Todo.objects.get(id=pk)
                form = TodoForm(request.POST, instance=todo)
            form.save()
            form = TodoForm()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            todo = Todo.objects.get(id=pk)
            todo.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            todo = Todo.objects.get(id=pk)
            form = TodoForm(instance=todo)

    context['form'] = form
    return render(request, 'index.html', context)


def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)
