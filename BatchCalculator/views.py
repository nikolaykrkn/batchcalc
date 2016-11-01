from django.shortcuts import render, redirect
from .models import rawMaterial
from django.views.generic import ListView, CreateView
from django import forms
from django.contrib.auth.models import User


class rawMaterialView(ListView):
	model = rawMaterial

def home(request):
	return render(request, 'BatchCalculator/home.html')

class addMaterial(CreateView):
    model = rawMaterial
    success_url = '/'
    fields = ('materialName', 'contentSiO2', 'contentAl2O3', 'contentNa2O')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(addMaterial, self).form_valid(form)