# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AgeGroup'
        db.create_table(u'schedule_agegroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('standings', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'schedule', ['AgeGroup'])

        # Adding model 'Team'
        db.create_table(u'schedule_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('park', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.Park'])),
            ('age_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.AgeGroup'])),
        ))
        db.send_create_signal(u'schedule', ['Team'])

        # Adding model 'Park'
        db.create_table(u'schedule_park', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('founded', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Park'])

        # Adding model 'Location'
        db.create_table(u'schedule_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Location'])

        # Adding model 'Competition'
        db.create_table(u'schedule_competition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'schedule', ['Competition'])

        # Adding M2M table for field age_groups on 'Competition'
        db.create_table(u'schedule_competition_age_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('competition', models.ForeignKey(orm[u'schedule.competition'], null=False)),
            ('agegroup', models.ForeignKey(orm[u'schedule.agegroup'], null=False))
        ))
        db.create_unique(u'schedule_competition_age_groups', ['competition_id', 'agegroup_id'])

        # Adding model 'Game'
        db.create_table(u'schedule_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('when', self.gf('django.db.models.fields.DateTimeField')()),
            ('age_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.AgeGroup'])),
            ('competition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.Competition'])),
            ('home_team', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='home_games', null=True, to=orm['schedule.Team'])),
            ('away_team', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='away_games', null=True, to=orm['schedule.Team'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('away_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schedule.Location'], null=True, blank=True)),
            ('bye', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'schedule', ['Game'])

        # Adding model 'ExtendedFlatPage'
        db.create_table(u'schedule_extendedflatpage', (
            (u'flatpage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['flatpages.FlatPage'], unique=True, primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['schedule.ExtendedFlatPage'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mptt_left', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('mptt_right', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('mptt_level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'schedule', ['ExtendedFlatPage'])


    def backwards(self, orm):
        # Deleting model 'AgeGroup'
        db.delete_table(u'schedule_agegroup')

        # Deleting model 'Team'
        db.delete_table(u'schedule_team')

        # Deleting model 'Park'
        db.delete_table(u'schedule_park')

        # Deleting model 'Location'
        db.delete_table(u'schedule_location')

        # Deleting model 'Competition'
        db.delete_table(u'schedule_competition')

        # Removing M2M table for field age_groups on 'Competition'
        db.delete_table('schedule_competition_age_groups')

        # Deleting model 'Game'
        db.delete_table(u'schedule_game')

        # Deleting model 'ExtendedFlatPage'
        db.delete_table(u'schedule_extendedflatpage')


    models = {
        u'flatpages.flatpage': {
            'Meta': {'ordering': "(u'url',)", 'object_name': 'FlatPage', 'db_table': "u'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
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
        u'schedule.extendedflatpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ExtendedFlatPage', '_ormbases': [u'flatpages.FlatPage']},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'flatpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['flatpages.FlatPage']", 'unique': 'True', 'primary_key': 'True'}),
            'mptt_left': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'mptt_level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'mptt_right': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['schedule.ExtendedFlatPage']"}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'schedule.game': {
            'Meta': {'ordering': "['id']", 'object_name': 'Game'},
            'age_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.AgeGroup']"}),
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'away_games'", 'null': 'True', 'to': u"orm['schedule.Team']"}),
            'bye': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Competition']"}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home_games'", 'null': 'True', 'to': u"orm['schedule.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Location']", 'null': 'True', 'blank': 'True'}),
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
            'Meta': {'ordering': "['name']", 'object_name': 'Park'},
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
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['schedule']