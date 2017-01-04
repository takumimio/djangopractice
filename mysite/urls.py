#from django.conf.urls import include, url
#from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^softjob/', include('ptt.urls')),
    url(r'^login/', 'mysite.views.user_login'),
    url(r'^logout/', 'mysite.views.user_logout'),
    url(r'^ajaxlogin/', 'mysite.views.ajax_login'),
)
