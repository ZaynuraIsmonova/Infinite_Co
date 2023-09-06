from django.db import models

# Create your models here.

class HomeModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return self.title


class ServicesModel(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=700)
    icons = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    

class AbilitiesModel(models.Model):
    title = models.CharField(max_length=250)
    percent = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class PortfoliosModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='projects/')
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class PartnersModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.title
    
    
class MessageModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=800)

    def __str__(self):
        return self.name

