from django.contrib import admin  # admin(module)
from .models import Product,Offer  #Product(class)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price' , 'stock') # the columns you want to display in the table

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount') # the columns you want to display in the table




admin.site.register(Product,ProductAdmin)   #Add a Products table from the models.py
admin.site.register(Offer,OfferAdmin)   #Add a Offers table from the models.py
