# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Park.founded'
        db.alter_column(u'schedule_park', 'founded', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Park.logo'
        db.alter_column(u'schedule_park', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Location.lat'
        db.alter_column(u'schedule_location', 'lat', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Location.lng'
        db.alter_column(u'schedule_location', 'lng', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'Park.founded'
        db.alter_column(u'schedule_park', 'founded', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Park.logo'
        db.alter_column(u'schedule_park', 'logo', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

        # Changing field 'Location.lat'
        db.alter_column(u'schedule_location', 'lat', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Location.lng'
        db.alter_column(u'schedule_location', 'lng', self.gf('django.db.models.fields.FloatField')(default=None))

    models = {
        u'schedule.agegroup': {
            'Meta': {'object_name': 'AgeGroup'},
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'when': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'schedule.location': {
            'Meta': {'object_name': 'Location'},
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
            'Meta': {'object_name': 'Team'},
            'age_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.AgeGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'park': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Park']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['schedule']