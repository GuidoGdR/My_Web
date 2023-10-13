from django.shortcuts import render

from apps.my_web_app.models import My_tool, Woroked_for_enterprice

"""
    Modificar la importacion del modelo post (desde la app blog) para evitarla y realizarlo mediante una peticion en el front
"""
from apps.blog.models import Post

# Create your views here.

def home(request):
    
    try:

        tools = My_tool.objects.all()
        woroked_for = Woroked_for_enterprice.objects.all()
        
        
    finally:
        pass
    
    contxt={
        "my_tools": tools,
        "woroked_for": woroked_for
    }
    
    
    return render(request, "my_web_app/home.html", contxt)
