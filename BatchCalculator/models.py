from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class rawMaterial(models.Model):
    materialName = models.CharField('Name of the Material', max_length=200, blank=False)
    contentSiO2 = models.FloatField('Content SiO2', default=0.0)
    contentAl2O3 = models.FloatField('Content of Al2O3', default=0.0)
    contentNa2O = models.FloatField('Content of Na2O', default=0.0)
    contentK2O = models.FloatField('Content of K2O', default=0.0)
    contentLi2O = models.FloatField('Content of Li2O',default=0.0)
    contentCaO = models.FloatField('Content of CaO', default=0.0)
    contentMgO = models.FloatField('Content of MgO', default=0.0)
    contentBaO = models.FloatField('Content of BaO', default=0.0)
    contentSrO = models.FloatField('Content of SrO', default=0.0)
    contentTiO2 = models.FloatField('Content of TiO2', default=0.0)
    contentZrO2 = models.FloatField('Content of ZrO2', default=0.0)
    contentB2O3 = models.FloatField('Content of B2O3', default=0.0)
    contentP2O5 = models.FloatField('Content of P2O5', default=0.0)
    contentZnO = models.FloatField('Content of ZnO', default=0.0)
    contentF = models.FloatField('Content of F', default=0.0)
    contentMnO = models.FloatField('Content of MnO', default=0.0)
    contentMoO3 = models.FloatField('Content of MoO3', default=0.0)
    contentNiO = models.FloatField('Content of NiO', default=0.0)
    contentCuO = models.FloatField('Content of CuO', default=0.0)
    contentCoO = models.FloatField('Content of CoO', default=0.0)
    contentFe2O3 = models.FloatField('Content of Fe2O3', default=0.0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
    	return self.materialName + ': '+'; '.join([str(getattr(self, attrName)) + ' ' + str(attrName).replace('content', '') \
    		for attrName in dir(rawMaterial) if attrName.startswith('content') and getattr(self, attrName) != 0.0])
