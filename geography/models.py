from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=400)
    capital = models.CharField(max_length=400)
    language = models.CharField(max_length=400)
    habitants = models.CharField(max_length=400)
    continent = models.CharField(max_length=255)
    square_kilometers = models.CharField(max_length=255)
    
    def __str__(self):
        return self.country

    

