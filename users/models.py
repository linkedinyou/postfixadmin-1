from django.db import models
from django.contrib import admin
from postfixadmin.domains.models import Domain
from hashlib import md5

class MD5EncryptedField(models.CharField):
    def save_form_data(self, instance, data):
        setattr(instance, self.name, md5(data).hexdigest())

class User(models.Model):
    domain = models.ForeignKey(Domain)
    name = models.CharField(max_length=80, null=False, verbose_name=u'full name')
    user = models.CharField(max_length=40, null=False, verbose_name=u'login')
    password = MD5EncryptedField(max_length=32, null=False)
    clearpw = models.CharField(max_length=32, null=False, verbose_name=u'clear password')
    quota = models.CharField(max_length=32, null=False, default='10485760')

    class Meta:
        verbose_name_plural = 'Users'

class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'user', 'domain', 'clearpw', 'quota')
    search_fields = ['domain', 'name', 'user']
    list_filter = ('domain', 'name', 'user')
    ordering = ['id']

admin.site.register(User, UserAdmin)
