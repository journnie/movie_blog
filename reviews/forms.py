from django import forms
from .models import Review


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie_title', 'review_title', 'content']
        widgets = {
            'movie_title': forms.TextInput(attrs={'placeholder': '리뷰할 영화 제목'}),
            'review_title': forms.TextInput(attrs={'placeholder': '리뷰 제목'}),
            'content': forms.Textarea(attrs={'placeholder': '리뷰 내용'})

        }