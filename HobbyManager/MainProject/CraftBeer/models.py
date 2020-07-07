from django.db import models


# Create your models here.
class Beer(models.Model):
    beer_name = models.CharField(max_length=75)
    brewery = models.CharField(max_length=50)
    style = models.CharField(max_length=20)
    abv = models.CharField(max_length=5)
    avg_score = models.DecimalField(decimal_places=10,max_digits=12)

    beers = models.Manager()

    def __str__(self):
        return self.beer_name
