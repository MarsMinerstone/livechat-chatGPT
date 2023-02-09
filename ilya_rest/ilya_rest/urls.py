"""ilya_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from rest_framework.routers import SimpleRouter

from orders.views import *
from django.contrib import admin
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings

#router = SimpleRouter()

#router.register('api/orders', OrderView)

urlpatterns = [
    #path('', orders_page),
    #path('orders_page/', orders_app),
    re_path('grappelli/', include('grappelli.urls')), # grappelli URLS
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('orders.urls')),
    re_path(r'^', include('products.urls')),
    re_path(r'^', include('main_app.urls')),
    re_path(r'^', include('dishes.urls')),
    
]

#urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)