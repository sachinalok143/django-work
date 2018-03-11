from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import (register_view,login_view,logout_view)


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact$', 'newsletter.views.contact', name='contact'),
    url(r'^navbar$', 'newsletter.views.navbar', name='navbar'),
    url(r'^add-item/$', 'newsletter.views.addItem', name='add-item'),
    url(r'^example-fluid$', 'newsletter.views.examplefluid', name='example-fluid'),
    url(r'^about$', 'tryDjango18.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),


]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
