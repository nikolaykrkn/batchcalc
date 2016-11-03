from django.shortcuts import render, redirect
from .models import rawMaterial
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class rawMaterialView(ListView):
	model = rawMaterial

def home(request):
	return render(request, 'BatchCalculator/home.html')

class addMaterial(CreateView):
    model = rawMaterial
    success_url = reverse_lazy('rawmateriallist')
    fields = ('materialName', 'contentSiO2', 'contentAl2O3', 'contentNa2O', 'contentK2O')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(addMaterial, self).form_valid(form)


class editMaterial(UpdateView):
	model=rawMaterial
	fields = ('materialName', 'contentSiO2', 'contentAl2O3', 'contentNa2O', 'contentK2O')
	success_url = 'raw-materials/'

class deleteMaterial(DeleteView):
	model=rawMaterial
	success_url = reverse_lazy('rawmateriallist')

def calculator(request):
	return render(request, 'BatchCalculator/input-glass.html')
