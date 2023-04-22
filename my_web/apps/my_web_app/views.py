from django.shortcuts import render

from apps.my_web_app.models import My_tool, Woroked_for_enterprice

"""
    Modificar la importacion del modelo post (desde la app blog) para evitarla y realizarlo mediante una peticion en el front
"""
from apps.blog.models import Post

# Create your views here.

def home(request):
    max_len_content_resume=300
    
    try:
        #posts = Post.objects.filter( posted=True ).order_by( "-id" )[:5]

        tools = My_tool.objects.all()
        woroked_for = Woroked_for_enterprice.objects.all()
        
        #Except ValueError inecesario: django resuelve solo
        """
        except ValueError:
            posts = Post.objects.filter( posted=True ).order_by( "id" )
            
        except Exception as e:
            print(type(e).__name__)
        """
        
    finally:
        pass
    
    #config:
    """
    #   Posts
    if type(posts).__name__ == "Post":
        posts = [posts]
    for post in posts:
        if post.content.__len__() > max_len_content_resume:
            post.content = post.content[ : max_len_content_resume ] + "..."
    """
    contxt={

        #"posts": posts,
        "my_tools": tools,
        "woroked_for": woroked_for
    }
    
    return render(request, "my_web_app/home.html", contxt)
