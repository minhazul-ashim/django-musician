from django.db import models

# Create your models here.
class Musician(models.Model) : 
    id = models.IntegerField(primary_key = True);
    firstName = models.CharField(max_length = 15);
    lastName = models.CharField(max_length = 15);
    email = models.EmailField(max_length = 30);
    phoneNumber = models.CharField(max_length = 20);
    instrumentType = models.CharField(max_length = 20);


class Album(models.Model) :
    id = models.IntegerField(primary_key = True);
    name = models.CharField(max_length = 25);
    releaseDate = models.DateField();
    rating = models.FloatField();
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)