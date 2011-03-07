from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url':'/admin/'}),
    (r'^media/(.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)
