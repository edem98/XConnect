from django.contrib import admin
from .models import Xmember
from django.utils.html import format_html


@admin.register(Xmember)
class XmemberAdmin(admin.ModelAdmin):
    """
       Administration class for clients in django admin panel
    """
    list_display = ['name', 'name', ]

    def name(self, obj):
        return obj.user.username
    name.short_description = "Username"

    def email(self, obj):
        return obj.user.username
    email.short_description = "Email"



