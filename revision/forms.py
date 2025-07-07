from django import forms
from .models import revision

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['title','subject','content','reviewed']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            
        }
