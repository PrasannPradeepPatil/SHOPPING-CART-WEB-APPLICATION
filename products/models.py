from django.db import models  #models(module)



class Product(models.Model):      #models.Model(class)
    name = models.CharField(max_length= 255)
    price= models.FloatField()
    stock = models.IntegerField()
    image_urls = models.CharField(max_length=2083)



                                 #from django.db import models(module)
class Offer(models.Model):      #models.Model(class)
    code = models.CharField(max_length= 10)
    description = models.CharField(max_length= 255)
    discount = models.FloatField()

