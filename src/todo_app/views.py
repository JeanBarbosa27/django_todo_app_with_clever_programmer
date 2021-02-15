from django.shortcuts import redirect, render

from .models import ToDo


def index(request):
    items_list = ToDo.objects.all().order_by('-created_at')

    context = {
        'items_list': items_list
    }

    return render(request, 'todo_app/pages/index.html', context)

def add_todo(request):
    if request.method == 'POST':
        item = request.POST['todo_item']
        ToDo.objects.create(title=item)

    return redirect('todo_app:index')

def delete_todo(request, item_id):
    if request.method == 'POST':
        item = ToDo.objects.get(id=item_id)
        item.delete()

    return redirect('todo_app:index')
