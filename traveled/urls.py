from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.homepage.urls')),
    path('', include('apps.destinations.urls')),
    path('', include('apps.packages.urls')),
    path('', include('apps.blogs.urls')),
    path('', include('apps.contacts.urls')),
    path('', include('apps.myuser.urls')),
    path('', include('apps.cartitems.urls')),
    path('', include('apps.aboutpage.urls')),
    path('', include('apps.booking.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
