from django.db import models

# Create your models here.
class Musician(models.Model) : 
    firstName = models.CharField(max_length = 15);
    lastName = models.CharField(max_length = 15);
    email = models.EmailField(max_length = 30);
    phoneNumber = models.CharField(max_length = 20);
    instrumentType = models.CharField(max_length = 20);

    # def __str__(self) -> str:
    #     return f"ID: {self.id} Name : {self.firstName} {self.lastName}"


class Album(models.Model) :
    name = models.CharField(max_length = 25);
    releaseDate = models.DateField();
    rating = models.FloatField();
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return f"ID: {self.id} Album : {self.name}"