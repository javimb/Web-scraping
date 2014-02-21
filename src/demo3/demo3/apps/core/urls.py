from django.conf.urls import url
from django.conf.urls import patterns

from .views import HomeView

urlpatterns = patterns('apps.core.views',
    url(r'^$',
        HomeView.as_view(),
        name='home'),
)
