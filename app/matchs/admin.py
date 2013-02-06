# coding: utf-8
from django.contrib import admin
from models import Match


# class PlayerMatchInline(admin.TabularInline):
#     model = PlayerMatch


# class MatchAdmin(admin.ModelAdmin):
#     inlines = [PlayerMatchInline, ]


admin.site.register(Match)
# admin.site.register(PlayerMatch)
