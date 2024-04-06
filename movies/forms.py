from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'title'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }

        error_messages = {
            'title': {'max_length': '입력 길이를 초과하였습니다'}
        }