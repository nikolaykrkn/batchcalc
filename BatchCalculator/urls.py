from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
				url(r'^raw-materials/$', views.rawMaterialView, name='rawmateriallist'),
				url(r'^add-material/$', views.addMaterial.as_view(), name='addmateriallist'),
				url(r'^edit/(?P<pk>\d+)/$', views.editMaterial.as_view(), name='editlist'),
				url(r'^delete/(?P<pk>\d+)/$', views.deleteMaterial.as_view(), name='deletelist'),
				url(r'^$', views.home, name='home'),
				url(r'^glass-composition/$', views.calculator, name='calculate'),
				url(r'^accounts/login/$', auth_views.login, name='login'),
				url(r'^accounts/logout/$', auth_views.logout, name='logout'),
              ]