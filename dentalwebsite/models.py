from django.db import models

# Create your models here.

class Form(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Form_one(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

