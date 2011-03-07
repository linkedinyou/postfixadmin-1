from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from postfixadmin.api.handlers import AutoResponseHandler

auth = HttpBasicAuthentication(realm="Postfix Admin")
ad = { 'authentication': auth }

autoresponse_handler = Resource(AutoResponseHandler)

urlpatterns = patterns('',
    url(r'^autoresponse/$', autoresponse_handler),
    url(r'^autoresponse/(?P<email>[^/]+)/$', autoresponse_handler),
)
