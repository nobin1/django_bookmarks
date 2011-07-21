# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Link.dances_whenever_able'
        db.add_column('bookmarks_link', 'dances_whenever_able', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Link.dances_whenever_able'
        db.delete_column('bookmarks_link', 'dances_whenever_able')


    models = {
        'bookmarks.link': {
            'Meta': {'object_name': 'Link'},
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['bookmarks']
