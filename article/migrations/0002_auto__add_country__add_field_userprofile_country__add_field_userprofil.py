# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('article_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iso', self.gf('django.db.models.fields.CharField')(default='IN', max_length=2, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='India', max_length=128)),
            ('printable_name', self.gf('django.db.models.fields.CharField')(default='India', max_length=128, null=True)),
            ('iso3', self.gf('django.db.models.fields.CharField')(default='IND', max_length=3, null=True)),
            ('numcode', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=91, null=True)),
        ))
        db.send_create_signal('article', ['Country'])

        # Adding field 'UserProfile.country'
        db.add_column('article_userprofile', 'country', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['article.Country']), keep_default=False)

        # Adding field 'UserProfile.profile_pic'
        db.add_column('article_userprofile', 'profile_pic', self.gf('django.db.models.fields.files.ImageField')(default='images/default_profile.png', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('article_country')

        # Deleting field 'UserProfile.country'
        db.delete_column('article_userprofile', 'country_id')

        # Deleting field 'UserProfile.profile_pic'
        db.delete_column('article_userprofile', 'profile_pic')


    models = {
        'article.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'default': "'IN'", 'max_length': '2', 'null': 'True'}),
            'iso3': ('django.db.models.fields.CharField', [], {'default': "'IND'", 'max_length': '3', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'India'", 'max_length': '128'}),
            'numcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '91', 'null': 'True'}),
            'printable_name': ('django.db.models.fields.CharField', [], {'default': "'India'", 'max_length': '128', 'null': 'True'})
        },
        'article.navigation': {
            'Meta': {'object_name': 'Navigation'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 9, 25, 2, 45, 59, 442548)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'article.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['article.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'default': "'images/default_profile.png'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['article']
