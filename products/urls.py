from django.urls import path #path(fn)
from . import views          #views(module)


urlpatterns = [
    path('', views.index),    #whenever  you  go to http://127.0.0.1:8000/products it will call index fn in views.py
    path('new', views.new) ##whenever  you  go to http://127.0.0.1:8000/products/new it will call new fn in views.py

]