from django import forms
from .models import Comment  # Comment 모델을 import

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Comment 모델을 사용
        fields = ['message']  # 'message' 필드만 사용

    # message 필드의 위젯 설정
    message = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 50,
            'class': 'form-control',
            'placeholder': '댓글을 입력하세요...'
        })
    )

