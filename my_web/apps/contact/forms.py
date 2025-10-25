
from django import forms


#investigar forms.ModelForm

class ContactForm(forms.Form):
    
    contact_mail = forms.EmailField(label="Mail:",required=False, max_length=5000)
    
    contact_message = forms.CharField(label="Mensaje*:", max_length=1000, required=True, widget=forms.Textarea())
    
    
    
    