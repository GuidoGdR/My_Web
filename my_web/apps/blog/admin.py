from django.contrib import admin

from apps.blog.models import Post, Topic, PostImage

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "resume", "date", "posted")
    search_fields = ("title",)
    list_filter = ("date", "posted")
    date_hierarchy = "date"
    

admin.site.register(Post, PostAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    

admin.site.register(Topic, TopicAdmin)

class ImgPostAdmin(admin.ModelAdmin):
    list_display = ("post", "img")
    search_fields = ("post",)
    
admin.site.register(PostImage, ImgPostAdmin)