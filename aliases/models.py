from django.db import models
from django.contrib import admin
from postfixadmin.domains.models import Domain

class Alias(models.Model):
    domain = models.ForeignKey(Domain)
    source = models.CharField(max_length=40, null=False, verbose_name=u'login', help_text='User without @domain')
    destination = models.EmailField(max_length=75, null=False)

    class Meta:
        verbose_name_plural = 'aliases'

class AliasAdmin(admin.ModelAdmin):

    list_display = ('source', 'domain', 'destination')
    search_fields = ['source', 'destination']
    list_filter = ('source', 'destination')
    ordering = ['id']

admin.site.register(Alias, AliasAdmin)
