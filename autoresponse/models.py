from django.db import models
from django.contrib import admin
from postfixadmin.users.models import User

class Response(models.Model):
    name = models.CharField(max_length=200)
    enabled = models.BooleanField(default=False)
    user = models.OneToOneField(User, related_name='User')

    def __unicode__(self):
        return self.name

admin.site.register(Response)
