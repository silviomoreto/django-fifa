# coding: utf-8
from django.contrib import admin
from models import Player, Team


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('victories', 'losses', 'ranking',)
    list_display = ('name', 'ranking', 'victories', 'losses')
    ordering = ['-ranking', '-victories']


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)
