# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field team_b on 'Match'
        db.delete_table('matchs_match_team_b')

        # Removing M2M table for field team_a on 'Match'
        db.delete_table('matchs_match_team_a')

        # Adding M2M table for field team_a_players on 'Match'
        db.create_table('matchs_match_team_a_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('match', models.ForeignKey(orm['matchs.match'], null=False)),
            ('player', models.ForeignKey(orm['players.player'], null=False))
        ))
        db.create_unique('matchs_match_team_a_players', ['match_id', 'player_id'])

        # Adding M2M table for field team_b_players on 'Match'
        db.create_table('matchs_match_team_b_players', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('match', models.ForeignKey(orm['matchs.match'], null=False)),
            ('player', models.ForeignKey(orm['players.player'], null=False))
        ))
        db.create_unique('matchs_match_team_b_players', ['match_id', 'player_id'])


    def backwards(self, orm):
        # Adding M2M table for field team_b on 'Match'
        db.create_table('matchs_match_team_b', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('match', models.ForeignKey(orm['matchs.match'], null=False)),
            ('player', models.ForeignKey(orm['players.player'], null=False))
        ))
        db.create_unique('matchs_match_team_b', ['match_id', 'player_id'])

        # Adding M2M table for field team_a on 'Match'
        db.create_table('matchs_match_team_a', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('match', models.ForeignKey(orm['matchs.match'], null=False)),
            ('player', models.ForeignKey(orm['players.player'], null=False))
        ))
        db.create_unique('matchs_match_team_a', ['match_id', 'player_id'])

        # Removing M2M table for field team_a_players on 'Match'
        db.delete_table('matchs_match_team_a_players')

        # Removing M2M table for field team_b_players on 'Match'
        db.delete_table('matchs_match_team_b_players')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'matchs.match': {
            'Meta': {'object_name': 'Match'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'team_a_players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_a_players'", 'symmetrical': 'False', 'to': "orm['players.Player']"}),
            'team_a_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_a_team'", 'to': "orm['players.Team']"}),
            'team_b_players': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'team_b_players'", 'symmetrical': 'False', 'to': "orm['players.Player']"}),
            'team_b_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_b_team'", 'to': "orm['players.Team']"}),
            'victory': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'players.player': {
            'Meta': {'object_name': 'Player'},
            'draws': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ranking': ('django.db.models.fields.IntegerField', [], {'default': '1200'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'victories': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'players.team': {
            'Meta': {'object_name': 'Team'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['matchs']