from django import urls
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from organisationconnect.sitemaps import PostSitemap
from ckeditor_uploader import views as ckeditor_views

from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import never_cache

from organisationconnect import views

sitemaps = {
    'posts': PostSitemap,
}

handler404 = views.error_404
handler500 = views.error_500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('magazine/', include('magazine.urls')),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('dashboard/', include('dashboard.urls')),
     path('chat/', include('chat.urls')),
     
    path('forum/', include('forum.urls')),
    path('search/', include('search.urls')),
    path('wiki/', include('wiki.urls')),
    path('members/', include('members.urls')),
 
    path(r'^tinymce/', include('tinymce.urls')),
    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



