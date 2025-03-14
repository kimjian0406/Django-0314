from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('todo/<int:todo_id>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
from django.urls import path
from . import views

urlpatterns = [
    # 기존 URL 패턴들...
    path('todo/<int:todo_id>/add_comment/', views.add_comment, name='add_comment'),  # 댓글 추가 페이지
]

from django.urls import path
from . import views

urlpatterns = [
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todo/<int:todo_id>/add_comment/', views.CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),
]

from django.urls import path
from . import views

urlpatterns = [
    # TodoDetailView
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),

    # Comment CRUD
    path('comment/<int:todo_id>/create/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Todo 상세 페이지
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),

    # 댓글 생성
    path('comment/<int:todo_id>/create/', views.CommentCreateView.as_view(), name='comment_create'),
    
    # 댓글 수정
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    
    # 댓글 삭제
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]

