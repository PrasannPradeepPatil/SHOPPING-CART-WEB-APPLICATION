from .models import Product,Offer  #Product(class) , Offer(class)
from django.shortcuts import render # render(fn)



def index(request):                   #request = url passed by urls.py
    products = Product.objects.all()  #all() returns all the objects in database ; filter() returns all the pbj in db by filtering ; grt() returns an particular object ; save() inserts object in DB
                                      #from django.shortcuts import render
    return render(request, 'index.html', {'products': products})#render(request ,'name of template',data to be passed to template)


def new(request):
    pass

