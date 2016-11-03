from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class rawMaterial(models.Model):
    materialName = models.CharField('Name of the Material', max_length=200, blank=False)
    contentSiO2 = models.DecimalField('Content SiO2', default=0.0, max_digits=5, decimal_places=2)
    contentAl2O3 = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    contentNa2O = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    contentK2O = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
    	return self.materialName + ': '+'; '.join([str(getattr(self, attrName)) + ' ' + str(attrName).replace('content', '') \
    		for attrName in dir(rawMaterial) if attrName.startswith('content') and getattr(self, attrName) != 0.0])
