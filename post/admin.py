from django.contrib import admin
from .models import Party

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    """
       Administration class for clients in django admin panel
    """
    list_display = ['organiser', 'city', 'title', 'image', 'description', 'location', 'title' ]


