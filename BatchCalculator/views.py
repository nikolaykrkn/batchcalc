from django.shortcuts import render
from BatchCalculator.models import rawMaterial
from django.views.generic import ListView

#class rawMaterialView(ListView):
    #model = rawMaterial
    #response = [rawMaterial.materialName, rawMaterial.contentAl2O3, rawMaterial.contentAl2O3, rawMaterial.contentNa2O]


def index(request):
    return render(request, 'BatchCalculator/index.html')
