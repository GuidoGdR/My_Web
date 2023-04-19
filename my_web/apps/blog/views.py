#from django.shortcuts import render
from django.http.response import JsonResponse

#from django.views import View
#from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Models and vars
from apps.blog.models import Post

# Forms
from apps.blog.forms import SerchBlogForm

# Create your views here.

class BlogView(ListView):
    
    model = Post
    queryset = Post.objects.filter( posted=True )
    context_object_name = "posts" # default: object_list
    
    template_name = "blog/blog.html"
    
    
    paginate_by = 5
    
    
    
    def setup(self, request, *args, **kwargs):
        return super().setup(request, *args, **kwargs)
    
    def get_queryset(self):
        return super().get_queryset()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        serch_blog_form = SerchBlogForm().as_p()
        context["serch_blog_form"] = serch_blog_form
        
        return context
    
    def get(self, request, *args, **kwargs):
        
        serch_title = request.GET.get("title")
        serch_topics = request.GET.getlist("topics")

        
        query = self.queryset
        
        if serch_title:
            
            if not serch_topics:
                query = query.filter(title__icontains = serch_title)
                
            else:
                
                query = query.filter( title__icontains = serch_title ) & query.filter( topic__in = serch_topics )
                    
                
        elif serch_topics:
            
            query = query.filter( topic__in = serch_topics ).distinct()
            
        
        self.queryset = query
        

        
        return super().get(request, *args, **kwargs)
    
class PostView(ListView):
    
    
    model = Post
    context_object_name = "post" # default: object_list
    
    template_name = "blog/post.html"
    
    post_id = 1
    
    """
    post_id = request.GET.get("post_id")
    if self.post_id:
        
        self.post_id = self.post_id.replace("/", "")

        if not ( self.post_id.isdecimal() ):
            self.post_id = 1
    else:
        self.post_id = 1
            
    """        
    
    def setup(self, request, *args, **kwargs):
         
        if request.method == "GET":
            
            post_id = request.GET.get("post_id")
            
            if post_id:
                post_id = post_id.replace("/", "")
                
                if post_id.isdecimal():
                    self.post_id = post_id
                
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):

        result = Post.objects.get( posted=True, pk=self.post_id )
        
        if result:
            return result
        
        else:
            return {
                "title": "Error!",
                "content": f"No se encontro ningun posts con el id {self.post_id}"
                }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["hola"] = "hola2"
        return context
    