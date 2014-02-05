# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Record'
        db.create_table(u'workout_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('altitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('distance', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('heart_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('position_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('position_long', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('speed', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='records', to=orm['workout.Workout'])),
        ))
        db.send_create_signal(u'workout', ['Record'])

        # Adding model 'Lap'
        db.create_table(u'workout_lap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('avg_heart_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('avg_speed', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('max_heart_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('max_speed', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_ascent', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_calories', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_distance', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_elapsed_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('total_timer_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('start_position_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('start_position_long', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('end_position_lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('end_position_long', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(related_name='laps', to=orm['workout.Workout'])),
        ))
        db.send_create_signal(u'workout', ['Lap'])

        # Adding field 'Workout.avg_heart_rate'
        db.add_column(u'workout_workout', 'avg_heart_rate',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.avg_speed'
        db.add_column(u'workout_workout', 'avg_speed',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.max_heart_rate'
        db.add_column(u'workout_workout', 'max_heart_rate',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.max_speed'
        db.add_column(u'workout_workout', 'max_speed',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.total_ascent'
        db.add_column(u'workout_workout', 'total_ascent',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.total_calories'
        db.add_column(u'workout_workout', 'total_calories',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.total_distance'
        db.add_column(u'workout_workout', 'total_distance',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.total_elapsed_time'
        db.add_column(u'workout_workout', 'total_elapsed_time',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.total_timer_time'
        db.add_column(u'workout_workout', 'total_timer_time',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.start_position_lat'
        db.add_column(u'workout_workout', 'start_position_lat',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.start_position_long'
        db.add_column(u'workout_workout', 'start_position_long',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.end_position_lat'
        db.add_column(u'workout_workout', 'end_position_lat',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Workout.end_position_long'
        db.add_column(u'workout_workout', 'end_position_long',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Record'
        db.delete_table(u'workout_record')

        # Deleting model 'Lap'
        db.delete_table(u'workout_lap')

        # Deleting field 'Workout.avg_heart_rate'
        db.delete_column(u'workout_workout', 'avg_heart_rate')

        # Deleting field 'Workout.avg_speed'
        db.delete_column(u'workout_workout', 'avg_speed')

        # Deleting field 'Workout.max_heart_rate'
        db.delete_column(u'workout_workout', 'max_heart_rate')

        # Deleting field 'Workout.max_speed'
        db.delete_column(u'workout_workout', 'max_speed')

        # Deleting field 'Workout.total_ascent'
        db.delete_column(u'workout_workout', 'total_ascent')

        # Deleting field 'Workout.total_calories'
        db.delete_column(u'workout_workout', 'total_calories')

        # Deleting field 'Workout.total_distance'
        db.delete_column(u'workout_workout', 'total_distance')

        # Deleting field 'Workout.total_elapsed_time'
        db.delete_column(u'workout_workout', 'total_elapsed_time')

        # Deleting field 'Workout.total_timer_time'
        db.delete_column(u'workout_workout', 'total_timer_time')

        # Deleting field 'Workout.start_position_lat'
        db.delete_column(u'workout_workout', 'start_position_lat')

        # Deleting field 'Workout.start_position_long'
        db.delete_column(u'workout_workout', 'start_position_long')

        # Deleting field 'Workout.end_position_lat'
        db.delete_column(u'workout_workout', 'end_position_lat')

        # Deleting field 'Workout.end_position_long'
        db.delete_column(u'workout_workout', 'end_position_long')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'workout.lap': {
            'Meta': {'object_name': 'Lap'},
            'avg_heart_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'end_position_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'end_position_long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_heart_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'max_speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'start_position_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'start_position_long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_ascent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_calories': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_elapsed_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_timer_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'laps'", 'to': u"orm['workout.Workout']"})
        },
        u'workout.record': {
            'Meta': {'object_name': 'Record'},
            'altitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'heart_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'position_long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'to': u"orm['workout.Workout']"})
        },
        u'workout.workout': {
            'Meta': {'object_name': 'Workout'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'avg_heart_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_position_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'end_position_long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            #'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'max_heart_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'max_speed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'start_position_lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'start_position_long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'total_ascent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_calories': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_distance': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_elapsed_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'total_timer_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'workouts'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['workout']
