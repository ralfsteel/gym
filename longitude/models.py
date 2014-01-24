from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=200)


    def __unicode__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    postal_area = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand)

    def __unicode__(self):
        return self.address




