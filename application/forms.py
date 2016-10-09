from django import forms
from django.forms import ModelForm
from application.models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
            model = Post
            fields = ('title','text')

