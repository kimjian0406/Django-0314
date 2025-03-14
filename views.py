from django.db.models import Prefetch
from django.shortcuts import render
from .models import Todo, Comment

def todo_detail(request, pk):
    todo = Todo.objects.prefetch_related(Prefetch('comments')).get(pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})
from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Todo

def add_comment(request, todo_id):
    todo = Todo.objects.get(id=todo_id)  # 특정 Todo 항목을 가져옵니다.
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 새로운 댓글을 저장합니다.
            comment = form.save(commit=False)
            comment.todo = todo  # 댓글을 해당 Todo와 연결
            comment.save()
            return redirect('todo_detail', todo_id=todo.id)  # 댓글 추가 후 Todo 상세 페이지로 리디렉션
    
    else:
        form = CommentForm()
    
    return render(request, 'todo/add_comment.html', {'form': form, 'todo': todo})

