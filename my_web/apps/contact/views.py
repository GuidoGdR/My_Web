#from django.shortcuts import render

#from django.views.generic.edit import CreateView
from os import environ
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail

from apps.contact.forms import ContactForm
from .tools import turnstileValidator

# Create your views here.

class ContactView(View):

    template_name = "contact/contact.html"

    def get(self, request, *args, **kwargs):
        
        form = ContactForm()
        contxt = {
            "contact_form": form
        }
        return render(request, "contact/form.html", contxt)
    
    def post(self, request, *args, **kwargs):

        contact_form = ContactForm(request.POST)

        form_is_valid=False
        if contact_form.is_valid():
            contact_form = contact_form.cleaned_data
            form_is_valid=True
        
        user_mail = contact_form.get("contact_mail")
        user_message = contact_form.get("contact_message")

        contxt = {
            "message": {
                "status": None,
                "title": None,
                "message": None,
                "user_mail": user_mail,
                "user_message": user_message
            }
        }

        turnstile_is_valid = turnstileValidator(request.POST.get("cf-turnstile-response"))

        if turnstile_is_valid and form_is_valid:
            
            mail_message = f"""
            Mail de contacto: {user_mail}.
            
            Mensaje:
            {user_message}
            
            """
            
            try:
                send_mail("Mensaje enviado desde Mi Web", mail_message, environ["EMAIL_HOST_USER"], [environ["SEND_MAIL_TO"]], fail_silently=False)
                contxt["message"]["status"] = "ok"
                contxt["message"]["title"] = "Mensaje enviado con exito!"
            except Exception as e:
                print(f"Error al intentar enviar mail!\ntipo:{e}\n\ndetalle:\n{e}")
                contxt["message"]["title"] = "Error interno!"
                contxt["message"]["status"] = "fail"
                contxt["message"]["message"] = "Ocurrio un fallo inesperado al intentar enviar el mensaje"

        elif not turnstile_is_valid:
            contxt["message"]["title"] = "Error al validar el CAPTCHA!"
            contxt["message"]["status"] = "fail"
            contxt["message"]["message"] = "Es posible que veas este error si te falto verificar no ser un robot o si volviste a enviar un formulario anterior apretando F5."
            
        else:
            contxt["message"]["title"] = "Error al intentar enviar el mensaje!"
            contxt["message"]["status"] = "fail"
            contxt["message"]["message"] = "El formulario no paso la validacion."
        
        return render(request, "contact/review.html", contxt)
        
        