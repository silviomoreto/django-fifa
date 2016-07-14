from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # url(r'^player/', include('app.players.urls')),
    # url(r'^matchs/', include('app.matchs.urls')),
    url(r'^', include(admin.site.urls)),
)
