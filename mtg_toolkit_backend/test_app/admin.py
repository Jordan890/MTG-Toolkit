from django.contrib import admin
from .models import Card
# Register your models here.

class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['cardName']}),
        (None,               {'fields': ['text']}),
        (None,               {'fields': ['type']}),
        (None,               {'fields': ['colors']})
    ]
    list_display = ('cardName', 'text', 'type', 'colors')
admin.site.register(Card, CardAdmin)