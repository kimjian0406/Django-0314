from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('todo/<int:todo_id>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

