from django.db import models

# Create your models here.


class TravelList(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=100)
    DestinationLocation = models.CharField(max_length=30)
    SourceLocation = models.CharField(max_length=30)
    Image = models.CharField(max_length=200)
    TripStartDate = models.DateField()
    TripEndDate = models.DateField()
    Accommodation = models.CharField(max_length=30)
    TripCost = models.DecimalField(max_digits=15, decimal_places=2)

    TravelLists = models.Manager()

    def __str__(self):
        return self.DestinationLocation





