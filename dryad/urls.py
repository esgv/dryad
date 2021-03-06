from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # wiki
    url(r'', include('dryad.wiki.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
