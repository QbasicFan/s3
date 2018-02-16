
from django.db import models
from .thingsList import color , posi
# Create your models here.



class front(models.Model):
    title = models.CharField(max_length=200)

    text = models.CharField(max_length=200)


    image = models.ImageField(upload_to='static/img/')

    position = models.CharField(default= "Middle" , max_length=100 , choices=posi)


    def __str__(self):
        return self.title


class section1(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    color = models.CharField(max_length=100 , choices=color)

    def __str__(self):
        return self.title


class section2(models.Model):
    title = models.CharField(max_length=200)

    text = models.CharField(max_length=200)
    subText = models.CharField(max_length=200)


    image = models.ImageField(upload_to='static/img/')



    def __str__(self):
        return self.title





