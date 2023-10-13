from django.urls import path

from apps.blog.apps import BlogConfig

from apps.blog.views import BlogView, PostView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('post/', PostView.as_view(), name="post")
]
