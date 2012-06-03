from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from core.views import logout_user
from core.views import logo_page
from core.views import prompt_calpoly
from core.views import gen_username
from core.views import select_class
from core.views import denied

admin.autodiscover()

handler404 = 'core.views.fourohfour'

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prompt-calpoly/$', prompt_calpoly),
    url(r'^select-class/$', select_class),
    url(r'^gen-username/$', gen_username),
    url(r'^denied/$', denied),
    url(r'^logout/$', logout_user),
    url(r'^$', logo_page),
)
