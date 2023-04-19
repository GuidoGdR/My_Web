from django.contrib import admin

from apps.my_web_app.models import My_tool, Woroked_for_enterprice

# Register your models here.


class Programming_language_admin(admin.ModelAdmin):
    list_display = ("name", "logo")
    search_fields = ("name",)

admin.site.register(My_tool, Programming_language_admin)

class Woroked_for_enterprice_admin(admin.ModelAdmin):
    list_display = ("name", "logo")
    search_fields = ("name",)

admin.site.register(Woroked_for_enterprice, Woroked_for_enterprice_admin)