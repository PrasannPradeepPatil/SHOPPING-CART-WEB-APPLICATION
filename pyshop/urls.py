"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin  #admin(class)
from django.urls import path      #path(fn)
from  django.urls import include  # include(fn)

urlpatterns = [
    path('admin/', admin.site.urls),                #whenever you go to http://127.0.0.1:8000/admin(inbuilt default app) go to admin.site.urls
    path('products/',include('products.urls')),     #whenever you go to http://127.0.0.1:8000/products go to products.urls
    path('products/new', include('products.urls'))  # whenever you go to http://127.0.0.1:8000/products/new go to products.urls
]
