# coding: utf-8
from datetime import datetime
from django.db import models
from players.models import Player, Team
from skills import Match as MatchElo
from skills.elo import EloCalculator, EloGameInfo


class Match(models.Model):
    FACTOR = 25
    BASE_ELO = 1200
    BETA = 200
    TEAM_A, TEAM_B = 'a', 'b'
    VICTORY_CHOICES = (
        (TEAM_A, u'Team A'),
        (TEAM_B, u'Team B'),
    )

    match_date = models.DateTimeField(u'match date', default=datetime.now)
    team_a_players = models.ManyToManyField(Player, related_name='team_a_players')
    team_a_team = models.ForeignKey(Team, related_name='team_a_team')
    team_b_players = models.ManyToManyField(Player, related_name='team_b_players')
    team_b_team = models.ForeignKey(Team, related_name='team_b_team')
    victory = models.CharField(u'victory', choices=VICTORY_CHOICES, max_length=1,
                               blank=True, null=True)

    class Meta:
        verbose_name, verbose_name_plural = u'match', u'matchs'

    def __unicode__(self):
        return '%s' % self.match_date

    def save(self, *args, **kwargs):
        obj = super(Match, self).save(*args, **kwargs)
        win = []
        loss = []
        if self.victory == self.TEAM_A:
            winners = self.team_a_players.all()
            lossers = self.team_b_players.all()
        elif self.victory == self.TEAM_B:
            winners = self.team_b_players.all()
            lossers = self.team_a_players.all()
        else:
            return obj

        for player in winners:
            player.victories += 1
            player.save()
            win.append((player.id, (player.ranking, self.FACTOR)))

        for player in lossers:
            player.losses += 1
            player.save()
            loss.append((player.id, (player.ranking, self.FACTOR)))

        # elo rating
        calculator = EloCalculator()
        game_info = EloGameInfo(self.BASE_ELO, self.BETA)

        teams = MatchElo([win, loss], [1, 2])
        new_ratings = calculator.new_ratings(teams, game_info)

        for player in winners:
            player.ranking = int(new_ratings.rating_by_id(player.id).mean)
            player.save()

        for player in lossers:
            player.ranking = int(new_ratings.rating_by_id(player.id).mean)
            player.save()

        return obj
