from django import forms
from .models import Topic, Comment

class CreateTopicForm(forms.ModelForm):
    # comment = forms.CharField(widget=forms.Textarea, label='Comment')
    class Meta:
        model = Topic
        fields = ['ttitle', 'tbody']

class CreateCommentForm(forms.ModelForm):
    # comment = forms.CharField(widget=forms.Textarea, label='Comment')
    class Meta:
        model = Comment
        fields = ['cbody']