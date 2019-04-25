from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^contact/', views.base, name = 'index'),
    url(r'^about/', views.about, name = 'about'),
    url(r'^signup/', views.base),
    url(r'^login/', views.base),
    url('', views.base),
]