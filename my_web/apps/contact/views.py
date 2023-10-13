#from django.shortcuts import render

#from django.views.generic.edit import CreateView
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail

from apps.contact.forms import ContactForm
# Create your views here.

class ContactView(View):
    """
    model = Post
    queryset = Post.objects.filter( posted=True )
    context_object_name = "posts" # default: object_list
    """
    
    template_name = "contact/contact.html"

    def get(self, request, *args, **kwargs):
        
        form = ContactForm()
        contxt = {
            "contact_form": form
        }
        return render(request, "contact/contact.html", contxt)
    
    def post(self, request, *args, **kwargs):
        
        contxt = {"message": {}}
        
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form = contact_form.cleaned_data
            
            user_mail = contact_form["contact_mail"]
            user_message = contact_form["contact_message"]
            
            message = f"""
            Mail de contacto: {user_mail}.
            
            Mensaje:
            {user_message}
            
            """
            
            #send_mail("Mensaje enviado desde Mi Web", message, "guidodoregoweb@gmail.com", ["guidodorego@gmail.com"], fail_silently=False)

            if user_mail:
                contxt["message"]["mail"] = user_mail
            
            if user_message:
                contxt["message"]["title"] = "Mensaje enviado con exito!"
                contxt["message"]["message"] = user_message
                contxt["message"]["status"] = "ok"
            
        else:
            user_mail = request.POST.get("contact_mail")
            user_message = request.POST.get("contact_message")
            contxt["message"]["title"] = "Error al intentar enviar el mensaje!"
            contxt["message"]["status"] = "fail"
            contxt["message"]["message"] = ["El formulario no paso la validacion.", f"mail = {user_mail}", f"mensaje = {user_message}"]
        
        return render(request, "contact/contact.html", contxt)
        
        