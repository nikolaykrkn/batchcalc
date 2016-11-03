from django.conf.urls import url
from . import views


urlpatterns = [
    			url(r'^raw-materials/$', views.rawMaterialView.as_view(), name='rawmateriallist'),
    			url(r'^add-material/$', views.addMaterial.as_view(), name='addmateriallist'),
    			url(r'^edit/(?P<pk>\d+)/$', views.editMaterial.as_view(), name='editlist'),
    			url(r'^delete/(?P<pk>\d+)/$', views.deleteMaterial.as_view(), name='deletelist'),
    			url(r'^$', views.home, name='home'),
    			url(r'^calculate-batch/$', views.calculator, name='calculate'),
              ]