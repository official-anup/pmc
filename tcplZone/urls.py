from django.contrib import admin
from django.urls import path, include
from TCPLapp import views
  
from django.conf import settings # new
from  django.conf.urls.static import static #new



urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('', include('TCPLapp.urls')),
    # path('',views.login,name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)