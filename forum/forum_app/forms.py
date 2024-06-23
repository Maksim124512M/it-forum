from django import forms
from .models import Comment


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['text']