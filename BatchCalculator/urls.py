from django.conf.urls import url
from . import views


urlpatterns = [
    			url(r'raw-materials/$', views.rawMaterialView.as_view(), name='rawmateriallist'),
    			url(r'add-material/$', views.addMaterial.as_view()),
    			url(r'^$', views.home),
              ]