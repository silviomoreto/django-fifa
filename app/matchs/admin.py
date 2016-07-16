# coding: utf-8
from django.contrib import admin
from models import Match


# class PlayerMatchInline(admin.TabularInline):
#     model = PlayerMatch


# class MatchAdmin(admin.ModelAdmin):
#     inlines = [PlayerMatchInline, ]

class MatchAdmin(admin.ModelAdmin):
    list_display = ['match_date', 'team_a_players_list', 'team_a_team', 'team_b_players_list', 'team_b_team', 'victory']
    list_filter = ('match_date', 'team_a_players', 'team_a_team', 'team_b_players', 'team_b_team', 'victory')
    search_fields = ['team_a_players', 'team_a_team', 'team_b_players', 'team_b_team', 'victory']

    def team_a_players_list(self, obj):

        if obj.team_a_players.all().count() > 0:
            return u', '.join(map(lambda x: x.name, obj.team_a_players.all()))
        else:
            return u'-'

    def team_b_players_list(self, obj):

        if obj.team_b_players.all().count() > 0:
            return u', '.join(map(lambda x: x.name, obj.team_b_players.all()))
        else:
            return u'-'

admin.site.register(Match, MatchAdmin)
# admin.site.register(PlayerMatch)
