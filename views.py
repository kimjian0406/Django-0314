from django.db.models import Prefetch
from django.shortcuts import render
from .models import Todo, Comment

def todo_detail(request, pk):
    todo = Todo.objects.prefetch_related(Prefetch('comments')).get(pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})

