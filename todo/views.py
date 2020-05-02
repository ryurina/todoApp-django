from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

def todoView(request):
    items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': items})

def addTodo(request):
    itemRequest = request.POST['content']
    newItem = TodoItem(content = itemRequest)
    newItem.save()
    return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
    itemToDelete = TodoItem.objects.get(id=todo_id)
    itemToDelete.delete()
    return HttpResponseRedirect('/')

