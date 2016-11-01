from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class rawMaterial(models.Model):
    materialName = models.CharField('Name of the Material', max_length=200, blank=False)
    contentSiO2 = models.FloatField('Content SiO2', default=0.0, max_length=5)
    contentAl2O3 = models.FloatField(default=0.0, max_length=5)
    contentNa2O = models.FloatField(default=0.0, max_length=5)
    contentK2O = models.FloatField(default=0.0, max_length=5)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
    	return self.materialName + ': '+'; '.join([str(getattr(self, attrName)) + ' ' + str(attrName).replace('content', '') \
    		for attrName in dir(rawMaterial) if attrName.startswith('content') and getattr(self, attrName) != 0.0])
