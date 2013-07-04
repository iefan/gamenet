from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def i18n_javascript(request):
    return admin.site.i18n_javascript(request)

urlpatterns = patterns(
    '',
    (r'^admin/jsi18n', i18n_javascript),
    url(r'^$', 'orderahead.views.gamedisplay'),
    url(r'^orderahead/$', 'orderahead.views.orderahead'),
    url(r'^select/$', 'orderahead.views.selectorder'),
    url(r'^about/$', 'orderahead.views.about'),
    url(r'^contact/$', 'orderahead.views.contact'),
    url(r'^order1step/$', 'orderahead.views.order1step'),
    url(r'^order2step/$', 'orderahead.views.order2step'),
    url(r'^order3step/$', 'orderahead.views.order3step'),
    url(r'^ordersubmit/$', 'orderahead.views.ordersubmit'),
    # Examples:
    # url(r'^$', 'gamenet.views.home', name='home'),
    # url(r'^gamenet/', include('gamenet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
