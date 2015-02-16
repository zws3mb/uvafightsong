from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fightsong.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^', include('round1.urls')),
#	(r'^$', RedirectView.as_view(url='/sprint1/list/')), # Just for ease of use.
    url(r'^admin/', include(admin.site.urls)),
)
