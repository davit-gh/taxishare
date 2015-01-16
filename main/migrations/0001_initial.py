# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("happenings", "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'MyProfile'
        db.create_table(u'main_myprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('balance', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
            ('mobile_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pin', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'main', ['MyProfile'])

        # Adding model 'SourceDest'
        db.create_table(u'main_sourcedest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(related_name='source_set', blank=True, to=orm['happenings.Streets'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(related_name='destination_set', blank=True, to=orm['happenings.Streets'])),
            ('book_date', self.gf('django.db.models.fields.DateField')()),
            ('timestamp', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'main', ['SourceDest'])

        # Adding model 'Feedback'
        db.create_table(u'main_feedback', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='event', to=orm['happenings.Event'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='usr', to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('feedback_desc', self.gf('django.db.models.fields.TextField')()),
            ('feedback_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Feedback'])

        # Adding model 'Contactus'
        db.create_table(u'main_contactus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('message_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Contactus'])

        # Adding model 'Inboundmail'
        db.create_table(u'main_inboundmail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('html_body', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('send_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('reply_to', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Inboundmail'])


    def backwards(self, orm):
        # Deleting model 'MyProfile'
        db.delete_table(u'main_myprofile')

        # Deleting model 'SourceDest'
        db.delete_table(u'main_sourcedest')

        # Deleting model 'Feedback'
        db.delete_table(u'main_feedback')

        # Deleting model 'Contactus'
        db.delete_table(u'main_contactus')

        # Deleting model 'Inboundmail'
        db.delete_table(u'main_inboundmail')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'happenings.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'happenings.event': {
            'Meta': {'object_name': 'Event'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "u'eeeeee'", 'max_length': '10'}),
            'background_color_custom': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['happenings.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'events'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'event_destination_set'", 'blank': 'True', 'to': u"orm['happenings.Streets']"}),
            'destination_detail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'end_repeat': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'font_color': ('django.db.models.fields.CharField', [], {'default': "u'000000'", 'max_length': '10'}),
            'font_color_custom': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['happenings.Location']", 'symmetrical': 'False', 'blank': 'True'}),
            'passanger_number': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'payment_method': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'repeat': ('django.db.models.fields.CharField', [], {'default': "u'NEVER'", 'max_length': '15'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'event_source_set'", 'blank': 'True', 'to': u"orm['happenings.Streets']"}),
            'source_detail': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['happenings.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'happenings.location': {
            'Meta': {'object_name': 'Location'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_line_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'})
        },
        u'happenings.streets': {
            'Meta': {'object_name': 'Streets'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_hy': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'happenings.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'main.contactus': {
            'Meta': {'object_name': 'Contactus'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'to': u"orm['happenings.Event']"}),
            'feedback_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feedback_desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'usr'", 'to': u"orm['auth.User']"})
        },
        u'main.inboundmail': {
            'Meta': {'object_name': 'Inboundmail'},
            'html_body': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reply_to': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.myprofile': {
            'Meta': {'object_name': 'MyProfile'},
            'balance': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pin': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'main.sourcedest': {
            'Meta': {'object_name': 'SourceDest'},
            'book_date': ('django.db.models.fields.DateField', [], {}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'destination_set'", 'blank': 'True', 'to': u"orm['happenings.Streets']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'source_set'", 'blank': 'True', 'to': u"orm['happenings.Streets']"}),
            'timestamp': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['main']