# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Game.name'
        db.delete_column(u'schedule_game', 'name')

        # Deleting field 'Game.slug'
        db.delete_column(u'schedule_game', 'slug')


    def backwards(self, orm):
        # Adding field 'Game.name'
        db.add_column(u'schedule_game', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Game.slug'
        db.add_column(u'schedule_game', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=1, max_length=50),
                      keep_default=False)


    models = {
        u'schedule.agegroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'AgeGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'standings': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'schedule.competition': {
            'Meta': {'object_name': 'Competition'},
            'age_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['schedule.AgeGroup']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'schedule.game': {
            'Meta': {'object_name': 'Game'},
            'age_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.AgeGroup']"}),
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_games'", 'to': u"orm['schedule.Team']"}),
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Competition']"}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_games'", 'to': u"orm['schedule.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'when': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'schedule.location': {
            'Meta': {'ordering': "['name']", 'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'schedule.park': {
            'Meta': {'object_name': 'Park'},
            'founded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'schedule.team': {
            'Meta': {'ordering': "['park__name', 'name']", 'object_name': 'Team'},
            'age_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.AgeGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'park': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Park']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['schedule']