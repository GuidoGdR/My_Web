from django.urls import path

from apps.my_web_app.apps import MyWebAppConfig

from apps.my_web_app.views import home

app_name = MyWebAppConfig.name

urlpatterns = [
    
    path('', home, name="home"),
]


