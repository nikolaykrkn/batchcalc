from django.shortcuts import render, redirect
from .models import rawMaterial
from django.views.generic import CreateView, UpdateView, DeleteView
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

class registerUser(CreateView):
	template_name='registration/register.html'
	form_class = UserCreationForm
	success_url='/'


def subscript(text):
	for letter in text:
		if letter.isnumeric():
			text = text.replace(letter, '<sub>' + letter + '</sub>')
	return text


matName = [str(attr) for attr in dir(rawMaterial) if (attr.startswith('material'))]
matOxides = [str(attr) for attr in dir(rawMaterial) if (attr.startswith('content'))]
tupleFields = tuple( matName + matOxides)
contextOxides = [str(attrName).replace('content', '') for attrName in dir(rawMaterial) if attrName.startswith('content')]
	

def Context_Materials(request):
	contextMaterials = []
	for material in rawMaterial.objects.filter(author=request.user.id):
		MaterialsObj = dict()
		MaterialsObj['Name'] = material.materialName
		MaterialsObj['id'] = material.id
		for oxide in matOxides:
			MaterialsObj[oxide] = getattr(material, str(oxide))
		contextMaterials.append(MaterialsObj)
	return contextMaterials


@login_required
def rawMaterialView(request):

	summaryList = []
	for elem in Context_Materials(request):
		oxideList = []
		for oxide in contextOxides:
			oxideList.append(elem['content'+oxide])
		summaryList.append((oxideList, elem['Name'], elem['id']))

	return render(request,
		'BatchCalculator/rawmaterial_list.html',
		{
			'oxideNames': [subscript(i) for i in contextOxides],
			'contentOxides': contextOxides,
			'compositions': summaryList,
		}
	)



class addMaterial(CreateView):
    model = rawMaterial
    success_url = reverse_lazy('rawmateriallist')
    fields = tupleFields
    def form_valid(self, form):
    	form.instance.author = self.request.user
    	return super(addMaterial, self).form_valid(form)

class editMaterial(UpdateView):
	model=rawMaterial
	fields = tupleFields
	success_url = reverse_lazy('rawmateriallist')

class deleteMaterial(DeleteView):
	model = rawMaterial
	success_url = reverse_lazy('rawmateriallist')

def home(request):
	return render(request, 'BatchCalculator/home.html')

@login_required
def calculator(request):
	return render(request, 'BatchCalculator/input-glass.html', {'oxides': contextOxides, 'materials': Context_Materials(request)})
