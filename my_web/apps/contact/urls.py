from django.urls import path

from apps.contact.apps import ContactConfig

from apps.contact.views import ContactView

app_name = ContactConfig.name

urlpatterns = [
    path('', ContactView.as_view(), name="contact")
]
