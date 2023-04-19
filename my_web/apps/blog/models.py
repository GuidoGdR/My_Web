from django.db import models

# Plugins
from ckeditor.fields import RichTextField
        
# Tools


def url_generator(self) -> str:
    post_name = self.post 
    url = f"img/{post_name}/{self.img.name}"
    
    return url

# Create your models here.

class PostImage(models.Model):

    def url_generator(self, file_name:str) -> str:
        file_suffix = file_name.rfind(".")
        file_suffix = file_name[file_suffix:]
        
        file_name = self.name + file_suffix
        
        post_name = str (self.post)
        while " " in post_name:
            post_name = post_name.replace(' ', '_')
        
        return f"img/post/{post_name}/{file_name}"
    
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Imagen para el post"
        verbose_name_plural = "Imagenes para los posts"
        
        #ordering = ['post']
        
    post = models.ForeignKey("blog.Post", verbose_name="Post", on_delete=models.CASCADE, null=False, blank=False)#on_delete=models.PROTECT
    
    name = models.CharField(verbose_name="Nombre", max_length=50, unique=True, null=False, blank=False,)
    
    img = models.ImageField(verbose_name="Imagen", upload_to=url_generator, height_field=None, width_field=None, max_length=None )
    
    

      
class Topic(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Tema")
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    
    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        
        ordering = ['id']
  


class Post(models.Model):
    
    title = models.CharField(max_length=100, verbose_name="Titulo")
    
    content = RichTextField(max_length=5000, verbose_name="Contenido")
    
    topic = models.ManyToManyField("blog.Topic", verbose_name=("Temas"), blank=True)#on_delete=models.PROTECT
    
    #img = models.("blog.Topic", verbose_name=("Imagenes"), blank=True)#on_delete=models.PROTECT
    
    date = models.DateField(verbose_name="Fecha")
    
    posted = models.BooleanField(verbose_name="Posteado") 
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    def resume(self):
        
        MAX_LENG_CONTENT_RESUME = 300

        resume = str (self.content)
        
        # Delete  <img alt="(...)/>
        ini_img = resume.find("<img alt=")
        while ini_img != -1:
            
            finish_img = resume[ini_img:].find("/>") + ini_img + 2
            
            resume = resume[:ini_img] + resume[finish_img:]
            
            ini_img = resume.find("<img alt=")
        
        # Apply max_leng_content_resume
        if resume.__len__() > MAX_LENG_CONTENT_RESUME:
            
            resume = resume[:MAX_LENG_CONTENT_RESUME]
            
            resume += "..."
            
        print (resume)
        
        return resume
     
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
        #db_table = "Post"
        
        ordering = ['-id']
