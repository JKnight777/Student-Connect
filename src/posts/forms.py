from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'text',
        ]