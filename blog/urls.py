#from django.conf.urls import url, patterns
#
#urlpatterns = patterns('blog.views',
#    url(r'^date$', 'date_actuelle'),
#    url(r'^welcome$', 'welcome'),
#	url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'),
#)
#
from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('blog.views',
    url(r'^$', 'accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', 'lire'),
    url(r'^contact/$', 'contact'),
    url(r'^voir_contacts/$', 'voir_contacts'),
)
