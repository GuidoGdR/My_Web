
from django import forms

from apps.blog.models import Topic


#investigar forms.ModelForm

class SerchBlogForm(forms.Form):
    
    title = forms.CharField(label="Titulo", max_length=100, required=False)
    
    #topics = forms.ModelChoiceField(label="Temas", queryset=Topic.objects.all(), required=False)
    
    topics = forms.ModelMultipleChoiceField(label="Temas", queryset=Topic.objects.all(), required=False)
    