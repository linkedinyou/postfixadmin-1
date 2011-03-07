from django.db import models
from django.contrib import admin

class Domain(models.Model):
    name = models.CharField(max_length=50)
    transport = models.CharField(max_length=80, null=False, default='virtual:')

    class Meta:
        verbose_name_plural = 'domains'

    def __unicode__(self):
        return self.name

class DomainAdmin(admin.ModelAdmin):

    list_display = ('name', 'transport')
    search_fields = ['name', 'transport']
    list_filter = ('name', 'transport')
    ordering = ['id']

admin.site.register(Domain, DomainAdmin)
