from django.conf.urls import url

from . import views
from BatchCalculator.views import rawMaterialView

urlpatterns = [
    			url(r'raw-materials/$', rawMaterialView.as_view()),
              ]